"""
Idiom Parser for UDweave Decoupled Access-Execute Constructs

This module provides parsing for idiom directives in UDweave source code that
enable decoupled access-execute optimizations. It extracts idiom constructs and
produces structured data while preserving the original source code for the
main UDweave parser.

Idioms are identified by the #pragma keyword followed by clauses (for, reduction,
onComplete) and Let/In blocks. The keyword can be changed without modifying
the internal representation.

Supported syntax patterns:

    Pattern 1 - Simple Let/In without loop (idiom1):
        #pragma onComplete(eventOnComplete, localvar)
        Let {
            long a = myArray[16];
            long b = myArray[6];
        }
        In {
            localvar = a + b;
        }

    Pattern 2 - For loop with reduction (idiom2):
        #pragma for reduction(+, sum) onComplete(eventOnComplete, sum)
        for(unsigned long i=0; i<LIMIT; i++) {
            Let {
                long a = myArrayA[i];
                long b = myArrayB[i];
            }
            In {
                sum = sum + a * b;
            }
        }

    Pattern 3 - For loop without reduction (idiom3):
        #pragma for onComplete(eventOnComplete)
        for(unsigned long i=0; i<LIMIT; i++) {
            Let {
                long a = myArrayA[i];
            }
            In {
                myArrayB[i] = a;
            }
        }

The parser produces a IdiomConstruct data structure containing:
    - has_loop: Whether this idiom has an associated for loop
    - for_loop: ForLoopSpec with loop variable, init, condition, increment
    - reductions: List of ReductionSpec with operator and variable
    - on_complete: OnCompleteSpec with event name and arguments
    - let_declarations: List of variable declarations from the Let block
    - in_body: Raw text content of the In block
    - request_in_flight: How many DRAM Accesses in flight at the same time
    - scratchpad_addr: A scratchpad address that can be used for transferring variables
    - num_lanes: Number of lanes to use for this idiom

Usage:
    from frontend.idiom_parser import IdiomParser

    parser = IdiomParser()
    clean_source, idioms = parser.process(source_code)

    # clean_source: Source code with idiom blocks removed (ready for main parser)
    # idioms: List of IdiomConstruct objects describing each idiom found

Author: UDweave Team
"""

import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


# =============================================================================
# Data Classes for Idiom Components
# =============================================================================

from enum import Enum, auto


class IndexType(Enum):
    """
    Classification of an array index expression.

    Used to categorize how an array is being indexed, which is important
    for code generation and optimization decisions.
    """
    CONSTANT = auto()     # A literal constant like 16, 0x10, etc.
    LOOP_VAR = auto()     # The loop iteration variable (e.g., 'i' in for(i=0; i<N; i++))
    VARIABLE = auto()     # A variable that is NOT the loop iterator
    EXPRESSION = auto()   # A complex expression (e.g., 'i + offset', 'i * 2')


@dataclass
class IndexExpr:
    """
    Represents a parsed array index expression.

    This class captures both the raw index expression and its classification,
    which helps determine how the array access should be handled during
    code generation.

    Attributes:
        raw_expr: The original index expression string (e.g., '16', 'i', 'i+1')
        index_type: Classification of the index (CONSTANT, LOOP_VAR, VARIABLE, EXPRESSION)
        constant_value: If index_type is CONSTANT, the numeric value (None otherwise)
        base_variable: For LOOP_VAR or VARIABLE, the variable name (None for CONSTANT/EXPRESSION)
        involves_loop_var: True if the expression uses the loop variable (even in EXPRESSION type)

    Examples:
        - "16" -> IndexExpr(raw_expr="16", index_type=CONSTANT, constant_value=16)
        - "i" -> IndexExpr(raw_expr="i", index_type=LOOP_VAR, base_variable="i")
        - "offset" -> IndexExpr(raw_expr="offset", index_type=VARIABLE, base_variable="offset")
        - "i+1" -> IndexExpr(raw_expr="i+1", index_type=EXPRESSION, involves_loop_var=True)
    """
    raw_expr: str
    index_type: IndexType
    constant_value: Optional[int] = None
    base_variable: Optional[str] = None
    involves_loop_var: bool = False

    def __repr__(self):
        if self.index_type == IndexType.CONSTANT:
            return f"IndexExpr(CONSTANT={self.constant_value})"
        elif self.index_type == IndexType.LOOP_VAR:
            return f"IndexExpr(LOOP_VAR='{self.base_variable}')"
        elif self.index_type == IndexType.VARIABLE:
            return f"IndexExpr(VARIABLE='{self.base_variable}')"
        else:
            loop_note = ", uses_loop_var" if self.involves_loop_var else ""
            return f"IndexExpr(EXPRESSION='{self.raw_expr}'{loop_note})"


@dataclass
class ArrayAccessExpr:
    """
    Represents a parsed array access expression (load from array).

    This captures the structure of an array access like myArray[i] or data[16],
    breaking it down into the array name and the parsed index.

    Attributes:
        array_name: The name of the array being accessed (e.g., 'myArray', 'data')
        index: The parsed index expression
        raw_expr: The original full expression string

    Example:
        "myArrayA[i]" -> ArrayAccessExpr(array_name="myArrayA", index=IndexExpr(LOOP_VAR='i'))
    """
    array_name: str
    index: IndexExpr
    raw_expr: str = ""

    def __repr__(self):
        return f"ArrayAccessExpr({self.array_name}[{self.index}])"


@dataclass
class VariableTypeInfo:
    """
    Stores type information for a variable extracted from surrounding code.

    This captures type information for variables declared outside the Let/In block,
    such as event parameters, thread-level variables, or local variables.

    Attributes:
        var_name: The variable name
        base_type: The base type (e.g., 'long', 'int', 'double')
        qualifiers: Type qualifiers (e.g., ['unsigned', 'const'])
        is_pointer: Whether this is a pointer type
        is_array: Whether this is an array type
        pointer_depth: Number of pointer indirections (e.g., 2 for 'int**')
        source: Where this type was found ('event_param', 'thread_var', 'local_var')

    Example:
        "long* myArrayB" -> VariableTypeInfo(
            var_name="myArrayB",
            base_type="long",
            is_pointer=True,
            pointer_depth=1,
            source="event_param"
        )
    """
    var_name: str
    base_type: str
    qualifiers: List[str] = field(default_factory=list)
    is_pointer: bool = False
    is_array: bool = False
    pointer_depth: int = 0
    source: str = ""  # 'event_param', 'thread_var', 'local_var'

    def full_type_str(self) -> str:
        """Return the full type string (e.g., 'unsigned long*')."""
        parts = []
        if self.qualifiers:
            parts.extend(self.qualifiers)
        parts.append(self.base_type)
        type_str = ' '.join(parts)
        if self.is_pointer:
            type_str += '*' * self.pointer_depth
        return type_str

    def __repr__(self):
        return f"TypeInfo({self.full_type_str()} {self.var_name}, source={self.source})"


@dataclass
class StoreOperation:
    """
    Represents a store operation in the In block (writing to an array).

    This captures statements like "myArrayB[i] = a;" where a value is being
    stored back to an array. This is important for identifying output arrays
    and their relationship to Let block variables.

    Attributes:
        array_name: The name of the array being written to
        index: The parsed index expression for the store location
        value_expr: The raw expression being stored (e.g., 'a', 'a + b')
        source_let_vars: List of Let variable names used in value_expr
        raw_statement: The original statement text
        array_type: Type information for the array (if available from context)

    Example:
        "myArrayB[i] = a;" -> StoreOperation(
            array_name="myArrayB",
            index=IndexExpr(LOOP_VAR='i'),
            value_expr="a",
            source_let_vars=["a"],
            array_type=VariableTypeInfo(base_type='long', is_pointer=True)
        )
    """
    array_name: str
    index: IndexExpr
    value_expr: str
    source_let_vars: List[str] = field(default_factory=list)
    raw_statement: str = ""
    array_type: Optional[VariableTypeInfo] = None

    def __repr__(self):
        vars_str = ', '.join(self.source_let_vars) if self.source_let_vars else 'none'
        type_str = f", type={self.array_type.full_type_str()}" if self.array_type else ""
        return f"StoreOperation({self.array_name}[{self.index}] = {self.value_expr}, from_let_vars=[{vars_str}]{type_str})"


# =============================================================================
# In-Block Expression Data Structures (for unrolling support)
# =============================================================================

class ExprType(Enum):
    """Type of expression node in the In-block expression tree."""
    VARIABLE = auto()      # A variable reference (e.g., 'sum', 'a', 'b')
    CONSTANT = auto()      # A literal constant (e.g., 42, 3.14)
    BINARY_OP = auto()     # Binary operation (e.g., a + b, a * b)
    UNARY_OP = auto()      # Unary operation (e.g., -a, !flag)
    FUNCTION_CALL = auto() # Function call (e.g., sqrt(x))


class BinaryOp(Enum):
    """Binary operators for In-block expressions."""
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'
    MOD = '%'
    BITAND = '&'
    BITOR = '|'
    BITXOR = '^'
    LSHIFT = '<<'
    RSHIFT = '>>'
    LT = '<'
    GT = '>'
    LE = '<='
    GE = '>='
    EQ = '=='
    NE = '!='
    LAND = '&&'
    LOR = '||'

    @classmethod
    def from_string(cls, op_str: str) -> Optional['BinaryOp']:
        """Convert operator string to BinaryOp enum."""
        for op in cls:
            if op.value == op_str:
                return op
        return None


class UnaryOp(Enum):
    """Unary operators for In-block expressions."""
    NEG = '-'      # Negation
    NOT = '!'      # Logical not
    BITNOT = '~'   # Bitwise not


@dataclass
class VariableInfo:
    """
    Information about a variable used in the In-block.

    Attributes:
        name: The variable name
        is_let_var: True if this variable was declared in the Let block
        let_decl: Reference to the LetDeclaration if is_let_var is True
        is_reduction_var: True if this is a reduction variable
        is_loop_var: True if this is the loop iteration variable
    """
    name: str
    is_let_var: bool = False
    let_decl: Optional['LetDeclaration'] = None
    is_reduction_var: bool = False
    is_loop_var: bool = False

    def __repr__(self):
        tags = []
        if self.is_let_var:
            tags.append("let")
        if self.is_reduction_var:
            tags.append("reduction")
        if self.is_loop_var:
            tags.append("loop")
        tag_str = f"[{','.join(tags)}]" if tags else ""
        return f"Var({self.name}{tag_str})"


@dataclass
class InBlockExpr:
    """
    Represents an expression node in the In-block expression tree.

    This recursive structure allows representing complex expressions like
    'sum + a * b' as a tree that can be traversed for code generation.

    Attributes:
        expr_type: The type of this expression node
        # For VARIABLE:
        var_info: Variable information (name, source, etc.)
        # For CONSTANT:
        constant_value: The literal value
        constant_type: Type of constant ('int', 'float', 'string')
        # For BINARY_OP:
        binary_op: The binary operator
        left: Left operand expression
        right: Right operand expression
        # For UNARY_OP:
        unary_op: The unary operator
        operand: The operand expression
        # For all:
        raw_text: Original text representation

    Example:
        Expression "sum + a * b" becomes:
        InBlockExpr(BINARY_OP, op=ADD,
            left=InBlockExpr(VARIABLE, var_info=Var("sum")),
            right=InBlockExpr(BINARY_OP, op=MUL,
                left=InBlockExpr(VARIABLE, var_info=Var("a")),
                right=InBlockExpr(VARIABLE, var_info=Var("b"))
            )
        )
    """
    expr_type: ExprType
    # For VARIABLE
    var_info: Optional[VariableInfo] = None
    # For CONSTANT
    constant_value: Optional[any] = None
    constant_type: str = ""
    # For BINARY_OP
    binary_op: Optional[BinaryOp] = None
    left: Optional['InBlockExpr'] = None
    right: Optional['InBlockExpr'] = None
    # For UNARY_OP
    unary_op: Optional[UnaryOp] = None
    operand: Optional['InBlockExpr'] = None
    # Original text
    raw_text: str = ""

    def get_all_variables(self) -> List[VariableInfo]:
        """Recursively collect all variables used in this expression."""
        variables = []
        if self.expr_type == ExprType.VARIABLE and self.var_info:
            variables.append(self.var_info)
        elif self.expr_type == ExprType.BINARY_OP:
            if self.left:
                variables.extend(self.left.get_all_variables())
            if self.right:
                variables.extend(self.right.get_all_variables())
        elif self.expr_type == ExprType.UNARY_OP and self.operand:
            variables.extend(self.operand.get_all_variables())
        return variables

    def get_let_variables(self) -> List[VariableInfo]:
        """Get only Let-declared variables from this expression."""
        return [v for v in self.get_all_variables() if v.is_let_var]

    def substitute_variable(self, var_name: str, replacement: str) -> str:
        """
        Generate expression string with a variable substituted.

        Args:
            var_name: The variable name to replace
            replacement: The replacement string

        Returns:
            Expression string with substitution applied
        """
        if self.expr_type == ExprType.VARIABLE:
            if self.var_info and self.var_info.name == var_name:
                return replacement
            return self.var_info.name if self.var_info else ""
        elif self.expr_type == ExprType.CONSTANT:
            return str(self.constant_value)
        elif self.expr_type == ExprType.BINARY_OP:
            left_str = self.left.substitute_variable(var_name, replacement) if self.left else ""
            right_str = self.right.substitute_variable(var_name, replacement) if self.right else ""
            op_str = self.binary_op.value if self.binary_op else "?"
            return f"({left_str} {op_str} {right_str})"
        elif self.expr_type == ExprType.UNARY_OP:
            op_str = self.unary_op.value if self.unary_op else "?"
            operand_str = self.operand.substitute_variable(var_name, replacement) if self.operand else ""
            return f"({op_str}{operand_str})"
        return self.raw_text

    def generate_with_substitutions(self, substitutions: dict) -> str:
        """
        Generate expression string with multiple variable substitutions.

        Args:
            substitutions: Dict mapping variable names to replacement strings

        Returns:
            Expression string with all substitutions applied
        """
        if self.expr_type == ExprType.VARIABLE:
            if self.var_info and self.var_info.name in substitutions:
                return substitutions[self.var_info.name]
            return self.var_info.name if self.var_info else ""
        elif self.expr_type == ExprType.CONSTANT:
            return str(self.constant_value)
        elif self.expr_type == ExprType.BINARY_OP:
            left_str = self.left.generate_with_substitutions(substitutions) if self.left else ""
            right_str = self.right.generate_with_substitutions(substitutions) if self.right else ""
            op_str = self.binary_op.value if self.binary_op else "?"
            return f"({left_str} {op_str} {right_str})"
        elif self.expr_type == ExprType.UNARY_OP:
            op_str = self.unary_op.value if self.unary_op else "?"
            operand_str = self.operand.generate_with_substitutions(substitutions) if self.operand else ""
            return f"({op_str}{operand_str})"
        return self.raw_text

    def __repr__(self):
        if self.expr_type == ExprType.VARIABLE:
            return f"Expr({self.var_info})"
        elif self.expr_type == ExprType.CONSTANT:
            return f"Expr({self.constant_value})"
        elif self.expr_type == ExprType.BINARY_OP:
            return f"Expr({self.left} {self.binary_op.value if self.binary_op else '?'} {self.right})"
        elif self.expr_type == ExprType.UNARY_OP:
            return f"Expr({self.unary_op.value if self.unary_op else '?'}{self.operand})"
        return f"Expr({self.raw_text})"


class AssignmentType(Enum):
    """Type of assignment in the In-block."""
    SIMPLE = '='       # x = expr
    ADD_ASSIGN = '+='  # x += expr
    SUB_ASSIGN = '-='  # x -= expr
    MUL_ASSIGN = '*='  # x *= expr
    DIV_ASSIGN = '/='  # x /= expr
    MOD_ASSIGN = '%='  # x %= expr
    AND_ASSIGN = '&='  # x &= expr
    OR_ASSIGN = '|='   # x |= expr
    XOR_ASSIGN = '^='  # x ^= expr


@dataclass
class InBlockStatement:
    """
    Represents a parsed statement from the In-block.

    Handles assignment statements like:
    - sum = sum + a * b;
    - result += value;
    - output[i] = computed;

    Attributes:
        target_var: The variable being assigned to
        target_is_array: True if assigning to an array element
        target_array_info: Array access info if target_is_array
        assignment_type: The type of assignment (=, +=, etc.)
        value_expr: The parsed expression tree for the RHS
        raw_statement: Original statement text
    """
    target_var: str
    target_is_array: bool = False
    target_array_info: Optional[ArrayAccessExpr] = None
    assignment_type: AssignmentType = AssignmentType.SIMPLE
    value_expr: Optional[InBlockExpr] = None
    raw_statement: str = ""

    def get_used_let_vars(self) -> List[str]:
        """Get names of Let variables used in this statement's value expression."""
        if self.value_expr:
            return [v.name for v in self.value_expr.get_let_variables()]
        return []

    def generate_unrolled(self, unroll_index: int, let_var_substitutions: dict) -> str:
        """
        Generate code for one iteration of an unrolled statement.

        Args:
            unroll_index: The unroll iteration index (0-7 for 8x unroll)
            let_var_substitutions: Dict mapping Let var names to their
                substitution patterns. Each pattern should have {i} placeholder.
                E.g., {'a': 'var{i}', 'b': '_var{i}'}

        Returns:
            Generated statement string for this unroll iteration
        """
        # Build substitutions for this specific index
        subs = {}
        for var_name, pattern in let_var_substitutions.items():
            subs[var_name] = pattern.format(i=unroll_index)

        # Generate the RHS expression with substitutions
        if self.value_expr:
            rhs = self.value_expr.generate_with_substitutions(subs)
        else:
            rhs = ""

        # Generate the full statement
        target = self.target_var
        op = self.assignment_type.value
        return f"{target} {op} {rhs};"

    def __repr__(self):
        return f"Statement({self.target_var} {self.assignment_type.value} {self.value_expr})"


@dataclass
class ParsedInBlock:
    """
    Container for the parsed In-block with support for unrolling.

    This class holds all parsed statements from the In-block and provides
    methods for code generation with loop unrolling.

    Attributes:
        statements: List of parsed statements
        raw_content: Original In-block content
        let_var_mapping: Maps Let variable names to their LetDeclaration
        reduction_vars: Set of reduction variable names

    Example Usage:
        parsed = idiom.parsed_in_block
        for stmt in parsed.statements:
            # Generate 8x unrolled code
            for i in range(8):
                code = stmt.generate_unrolled(i, {
                    'a': 'var{i}',      # a comes from first-returned read
                    'b': '_var{i}'      # b comes from event params
                })
                print(code)
    """
    statements: List[InBlockStatement] = field(default_factory=list)
    raw_content: str = ""
    let_var_mapping: dict = field(default_factory=dict)  # var_name -> LetDeclaration
    reduction_vars: set = field(default_factory=set)

    def generate_unrolled_block(self, unroll_factor: int,
                                 let_var_substitutions: dict,
                                 indent: str = "    ") -> str:
        """
        Generate fully unrolled In-block code.

        Args:
            unroll_factor: Number of times to unroll (e.g., 8)
            let_var_substitutions: Dict mapping Let var names to substitution patterns
            indent: Indentation string for each line

        Returns:
            Multi-line string with unrolled code
        """
        lines = []
        for stmt in self.statements:
            for i in range(unroll_factor):
                line = stmt.generate_unrolled(i, let_var_substitutions)
                lines.append(f"{indent}{line}")
        return "\n".join(lines)

    def get_all_let_vars_used(self) -> set:
        """Get all Let variable names used across all statements."""
        vars_used = set()
        for stmt in self.statements:
            vars_used.update(stmt.get_used_let_vars())
        return vars_used

    def __repr__(self):
        return f"ParsedInBlock({len(self.statements)} statements)"


@dataclass
class LetDeclaration:
    """
    Represents a variable declaration in a Let block.

    The Let block declares variables that will be loaded from memory arrays.
    Each declaration maps a local variable to a source expression (typically
    an array access like myArray[i]).

    Attributes:
        var_type: The base type (e.g., 'long', 'int', 'double')
        var_name: The variable name being declared
        source_expr: The raw source expression string (e.g., 'myArray[i]', 'data[16]')
        parsed_source: Parsed representation of the source expression (ArrayAccessExpr)
        is_pointer: Whether this is a pointer declaration (*)
        is_local_pointer: Whether this is a local/scratchpad pointer (*local)
        qualifiers: List of type qualifiers (e.g., ['unsigned', 'const'])
        raw_declaration: The original declaration text for debugging
    """
    var_type: str
    var_name: str
    source_expr: str
    parsed_source: Optional[ArrayAccessExpr] = None
    is_pointer: bool = False
    is_local_pointer: bool = False
    qualifiers: List[str] = field(default_factory=list)
    raw_declaration: str = ""

    def __repr__(self):
        qual_str = ' '.join(self.qualifiers) + ' ' if self.qualifiers else ''
        ptr_str = '*local ' if self.is_local_pointer else ('*' if self.is_pointer else '')
        return f"LetDeclaration({qual_str}{self.var_type} {ptr_str}{self.var_name} = {self.source_expr})"


@dataclass
class ReductionSpec:
    """
    Represents a reduction specification in an idiom construct.

    Reductions accumulate values across iterations using an associative operator.
    Common examples: sum (+), product (*), bitwise AND (&), bitwise OR (|).

    Attributes:
        operator: The reduction operator ('+', '-', '*', '/', '&', '|', '^')
        variable: The variable that accumulates the reduction result
    """
    operator: str
    variable: str

    def __repr__(self):
        return f"ReductionSpec(op='{self.operator}', var='{self.variable}')"


@dataclass
class OnCompleteSpec:
    """
    Represents an onComplete callback specification.

    The onComplete event is called when all iterations of the idiom construct
    have finished executing. It can receive arguments (typically the reduction
    result or other computed values).

    Attributes:
        event_name: The name of the event to call on completion (may include namespace)
        arguments: List of argument names to pass to the event
    """
    event_name: str
    arguments: List[str] = field(default_factory=list)

    def __repr__(self):
        args = ', '.join(self.arguments)
        return f"OnCompleteSpec(event='{self.event_name}', args=[{args}])"


@dataclass
class LoopBound:
    """
    Represents a parsed loop bound (start or end value).

    Attributes:
        raw_expr: The original expression string
        is_constant: True if the bound is a compile-time constant
        constant_value: The integer value if is_constant is True
        variable_name: The variable/macro name if not a constant (e.g., 'LIMIT')
    """
    raw_expr: str
    is_constant: bool = False
    constant_value: Optional[int] = None
    variable_name: Optional[str] = None

    def __repr__(self):
        if self.is_constant:
            return f"LoopBound({self.constant_value})"
        elif self.variable_name:
            return f"LoopBound(var={self.variable_name})"
        else:
            return f"LoopBound(expr='{self.raw_expr}')"


@dataclass
class LoopStride:
    """
    Represents the parsed stride/step of a loop.

    Attributes:
        raw_expr: The original increment expression string
        is_constant: True if the stride is a compile-time constant
        constant_value: The integer stride value if is_constant (e.g., 1 for i++, -1 for i--)
        variable_name: The variable name if stride depends on a variable
        direction: 1 for increasing, -1 for decreasing, 0 for unknown
    """
    raw_expr: str
    is_constant: bool = False
    constant_value: Optional[int] = None
    variable_name: Optional[str] = None
    direction: int = 1  # 1 = increasing, -1 = decreasing, 0 = unknown

    def __repr__(self):
        if self.is_constant:
            return f"LoopStride({self.constant_value})"
        elif self.variable_name:
            return f"LoopStride(var={self.variable_name})"
        else:
            return f"LoopStride(expr='{self.raw_expr}')"


@dataclass
class ForLoopSpec:
    """
    Represents the for loop specification associated with an idiom construct.

    This captures the loop header components for code generation.
    Example: for(unsigned long i=0; i<LIMIT; i++)

    Attributes:
        var_type: The loop variable type (e.g., 'long', 'int')
        var_qualifiers: Type qualifiers (e.g., ['unsigned'])
        var_name: The loop variable name (e.g., 'i')

        # Raw string representations
        raw_init: The raw initialization expression (e.g., '0')
        raw_condition: The raw loop condition expression (e.g., 'i<LIMIT')
        raw_increment: The raw increment expression (e.g., 'i++')
        raw_header: The original for loop header text

        # Parsed structured values
        start: LoopBound with parsed start value
        end: LoopBound with parsed end value/variable
        comparison_op: The comparison operator ('<', '<=', '>', '>=', '!=')
        stride: LoopStride with parsed stride information
    """
    var_type: str
    var_qualifiers: List[str]
    var_name: str

    # Raw strings
    raw_init: str
    raw_condition: str
    raw_increment: str
    raw_header: str = ""

    # Parsed values
    start: Optional[LoopBound] = None
    end: Optional[LoopBound] = None
    comparison_op: str = "<"
    stride: Optional[LoopStride] = None

    def __repr__(self):
        quals = ' '.join(self.var_qualifiers) + ' ' if self.var_qualifiers else ''
        return f"ForLoopSpec({quals}{self.var_type} {self.var_name}={self.raw_init}; {self.raw_condition}; {self.raw_increment})"


@dataclass
class IdiomConstruct:
    """
    Complete representation of a decoupled access-execute idiom construct.

    This is the main data structure returned by the parser. It contains all
    information needed for code generation of decoupled access-execute patterns.

    Attributes:
        has_loop: True if this idiom has an associated for loop
        for_loop: ForLoopSpec with loop details (None if has_loop is False)
        reductions: List of ReductionSpec (multiple reductions allowed)
        on_complete: OnCompleteSpec for the completion callback (required)
        let_declarations: List of variable declarations from the Let block
        let_block_raw: Raw text of the Let block content
        in_body: Raw text content of the In block (the computation)
        parsed_in_block: Parsed representation of the In block for unrolling
        store_operations: List of array store operations found in the In block
        start_line: Line number where the idiom starts
        end_line: Line number where the idiom ends
        original_text: The original idiom text for debugging

    Example usage:
        if idiom.has_loop:
            print(f"Loop variable: {idiom.for_loop.var_name}")
            print(f"Iterating while: {idiom.for_loop.raw_condition}")
        for red in idiom.reductions:
            print(f"Reducing with {red.operator} into {red.variable}")
        for store in idiom.store_operations:
            print(f"Store to {store.array_name}[{store.index}] from Let vars: {store.source_let_vars}")

        # Generate unrolled code:
        if idiom.parsed_in_block:
            code = idiom.parsed_in_block.generate_unrolled_block(8, {'a': 'var{i}', 'b': '_var{i}'})
    """
    has_loop: bool = False
    for_loop: Optional[ForLoopSpec] = None
    reductions: List[ReductionSpec] = field(default_factory=list)  # Multiple reductions allowed
    on_complete: Optional[OnCompleteSpec] = None
    let_declarations: List[LetDeclaration] = field(default_factory=list)
    let_block_raw: str = ""
    in_body: str = ""
    parsed_in_block: Optional[ParsedInBlock] = None
    store_operations: List[StoreOperation] = field(default_factory=list)
    type_context: Dict[str, VariableTypeInfo] = field(default_factory=dict)  # External variable types
    start_line: int = 0
    end_line: int = 0
    original_text: str = ""
    num_lanes: int = 1
    scratchpad_offset: Optional[str] = None
    max_requests_in_flight: Optional[int] = None

    def get_let_var_names(self) -> List[str]:
        """Return list of variable names declared in Let block."""
        return [decl.var_name for decl in self.let_declarations]

    def get_let_sources(self) -> dict:
        """
        Return mapping of Let variable names to their source expressions.

        Returns:
            Dictionary mapping variable name to source expression
            Example: {'a': 'myArray[i]', 'b': 'myArray[i]'}
        """
        return {decl.var_name: decl.source_expr for decl in self.let_declarations}

    def get_loop_var(self) -> Optional[str]:
        """Return the loop variable name, or None if no loop."""
        return self.for_loop.var_name if self.for_loop else None

    def get_dependencies(self) -> dict:
        """
        Analyze dependencies between Let variables, loop variable, and In block.

        This performs a simple lexical analysis to find which variables
        are used in the In block. For more sophisticated analysis, the
        caller should use the AST.

        Returns:
            Dictionary with:
                - 'let_vars': Set of variables declared in Let block
                - 'let_var_types': Dict mapping Let var names to their types
                - 'loop_var': The loop variable name (if any)
                - 'loop_var_type': The loop variable type (if any)
                - 'in_all_vars': Set of all variables/identifiers used in In block
                - 'in_uses_let_vars': Set of Let variables used in In block
                - 'in_uses_loop_var': Whether the loop variable is used in In block
                - 'in_other_vars': Set of variables in In block that are not Let/loop vars
                - 'in_other_var_types': Dict mapping other var names to VariableTypeInfo (from context)
                - 'reduction_vars': List of reduction variables (multiple allowed)
                - 'reduction_var_types': Dict mapping reduction var names to types (from context)
        """
        let_vars = set(self.get_let_var_names())
        loop_var = self.get_loop_var()
        in_all_vars = set()
        in_uses_let_vars = set()
        in_uses_loop_var = False
        in_other_vars = set()

        # Build type info for Let variables from declarations
        let_var_types = {}
        for decl in self.let_declarations:
            qual_str = ' '.join(decl.qualifiers) + ' ' if decl.qualifiers else ''
            ptr_str = '*local' if decl.is_local_pointer else ('*' if decl.is_pointer else '')
            let_var_types[decl.var_name] = f"{qual_str}{decl.var_type}{ptr_str}".strip()

        # Loop variable type
        loop_var_type = None
        if self.for_loop:
            qual_str = ' '.join(self.for_loop.var_qualifiers) + ' ' if self.for_loop.var_qualifiers else ''
            loop_var_type = f"{qual_str}{self.for_loop.var_type}".strip()

        # Keywords to exclude from variable detection
        keywords = {
            'if', 'else', 'for', 'while', 'do', 'switch', 'case', 'default',
            'break', 'continue', 'return', 'goto', 'sizeof', 'typedef',
            'struct', 'union', 'enum', 'const', 'static', 'extern', 'volatile',
            'register', 'auto', 'signed', 'unsigned', 'void',
            'char', 'short', 'int', 'long', 'float', 'double', 'bool',
            'true', 'false', 'NULL', 'nullptr'
        }

        # Simple regex to find identifiers in the In block
        if self.in_body:
            identifiers = re.findall(r'\b([a-zA-Z_][a-zA-Z_0-9]*)\b', self.in_body)
            # Filter out keywords
            in_all_vars = set(identifiers) - keywords
            # Let variables used in In block
            in_uses_let_vars = let_vars.intersection(in_all_vars)
            # Check if loop variable is used
            if loop_var:
                in_uses_loop_var = loop_var in in_all_vars
            # Other variables (not Let vars, not loop var)
            in_other_vars = in_all_vars - let_vars
            if loop_var:
                in_other_vars = in_other_vars - {loop_var}

        # Collect all reduction variables
        reduction_vars = [r.variable for r in self.reductions] if self.reductions else []

        # Build type info for other variables from type_context
        in_other_var_types = {}
        for var_name in in_other_vars:
            if var_name in self.type_context:
                in_other_var_types[var_name] = self.type_context[var_name]

        # Build type info for reduction variables from type_context
        reduction_var_types = {}
        for var_name in reduction_vars:
            if var_name in self.type_context:
                reduction_var_types[var_name] = self.type_context[var_name]

        return {
            'let_vars': let_vars,
            'let_var_types': let_var_types,
            'loop_var': loop_var,
            'loop_var_type': loop_var_type,
            'in_all_vars': in_all_vars,
            'in_uses_let_vars': in_uses_let_vars,
            'in_uses_loop_var': in_uses_loop_var,
            'in_other_vars': in_other_vars,
            'in_other_var_types': in_other_var_types,
            'reduction_vars': reduction_vars,
            'reduction_var_types': reduction_var_types
        }

    def __repr__(self):
        parts = ["IdiomConstruct("]
        parts.append(f"  has_loop={self.has_loop}")
        if self.for_loop:
            parts.append(f"  for_loop={self.for_loop}")
        if self.reductions:
            parts.append(f"  reductions={self.reductions}")
        if self.on_complete:
            parts.append(f"  on_complete={self.on_complete}")
        if self.let_declarations:
            parts.append(f"  let_declarations={self.let_declarations}")
        if self.in_body:
            body_preview = self.in_body[:50] + "..." if len(self.in_body) > 50 else self.in_body
            body_preview = body_preview.replace('\n', '\\n')
            parts.append(f"  in_body='{body_preview}'")
        parts.append(")")
        return '\n'.join(parts)


# =============================================================================
# Main Parser Class
# =============================================================================

class IdiomParser:
    """
    Parser that extracts idiom constructs from UDweave source.

    This class provides the main interface for processing UDWeave source code.
    It finds all idiom blocks (marked with #pragma), parses them into structured
    data, and returns both the cleaned source code and the structured data.

    The parser handles two main patterns:
        1. Idiom with for loop - iteration over arrays with Let/In blocks
        2. Idiom without loop - single Let/In block for point access

    Usage:
        parser = IdiomParser()
        clean_source, idioms = parser.process(source_code)
    """

    # -------------------------------------------------------------------------
    # Regex patterns for parsing idiom components
    # -------------------------------------------------------------------------

    # Pattern for reduction clause: reduction(op, var)
    # Matches: reduction(+, sum), reduction(*, product), etc.
    REDUCTION_PATTERN = re.compile(
        r'reduction\s*\(\s*([+\-*/&|^])\s*,\s*([a-zA-Z_][a-zA-Z_0-9]*)\s*\)'
    )

    # Pattern for onComplete clause: onComplete(event, arg1, arg2, ...)
    # Event name can include namespace (e.g., myThread::myEvent)
    # Arguments are optional
    ONCOMPLETE_PATTERN = re.compile(
        r'onComplete\s*\(\s*'
        r'([a-zA-Z_][a-zA-Z_0-9]*(?:::[a-zA-Z_][a-zA-Z_0-9]*)*)'  # Event name
        r'(?:\s*,\s*([^)]+))?'  # Optional arguments
        r'\s*\)'
    )

    # Pattern for variable declaration in Let block
    # Handles: type var = expr;  or  type *var = expr;  or  type *local var = expr;
    # Type can have qualifiers like 'unsigned long'
    LET_DECL_PATTERN = re.compile(
        r'^\s*'
        r'((?:unsigned\s+|const\s+)*)'                    # Optional qualifiers
        r'(char|short|int|long|float|double)\s+'          # Base type
        r'(\*\s*local\s+|\*\s*)?'                          # Optional pointer specifier
        r'([a-zA-Z_][a-zA-Z_0-9]*)\s*'                     # Variable name
        r'=\s*'                                            # Assignment operator
        r'(.+?)\s*;',                                      # Expression and semicolon
        re.MULTILINE
    )

    # Pattern for parsing for loop header
    # Matches: for(type var = init; condition; increment)
    # Example: for(unsigned long i=0; i<LIMIT; i++)
    FOR_LOOP_PATTERN = re.compile(
        r'for\s*\(\s*'
        r'((?:unsigned\s+|const\s+)*)'                    # Optional qualifiers
        r'(char|short|int|long|float|double)\s+'          # Base type
        r'([a-zA-Z_][a-zA-Z_0-9]*)\s*'                     # Variable name
        r'=\s*([^;]+)\s*;\s*'                              # Init expression
        r'([^;]+)\s*;\s*'                                  # Condition
        r'([^)]+)\s*'                                      # Increment
        r'\)'
    )

    # Pattern for array access: arrayName[index]
    # Captures the array name and the index expression
    ARRAY_ACCESS_PATTERN = re.compile(
        r'([a-zA-Z_][a-zA-Z_0-9]*)\s*\[\s*([^]]+)\s*]'
    )

    # Pattern for array store in In block: array[index] = value;
    # Captures the array name, index, and value expression
    ARRAY_STORE_PATTERN = re.compile(
        r'([a-zA-Z_][a-zA-Z_0-9]*)\s*\[\s*([^]]+)\s*]\s*=\s*([^;]+)\s*;'
    )

    # Pattern to detect if an expression is a simple integer constant
    # Matches: decimal (123), hex (0x1F), binary (0b1010), octal (0777)
    INTEGER_CONSTANT_PATTERN = re.compile(
        r'^(0x[0-9a-fA-F]+|0b[01]+|0[0-7]+|[0-9]+)$'
    )

    # Pattern to detect if an expression is a simple identifier (variable name)
    IDENTIFIER_PATTERN = re.compile(
        r'^([a-zA-Z_][a-zA-Z_0-9]*)$'
    )

    # Pattern for event declaration parameters: event name(type1 var1, type2* var2, ...)
    # Captures the full parameter list for further parsing
    EVENT_DECL_PATTERN = re.compile(
        r'event\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(([^)]*)\)\s*\{'
    )

    # Pattern for a single parameter in an event/function declaration
    # Handles: type var, type* var, unsigned long* var, etc.
    PARAM_DECL_PATTERN = re.compile(
        r'((?:unsigned\s+|const\s+|static\s+)*)'   # Optional qualifiers
        r'(char|short|int|long|float|double|void)\s*'  # Base type
        r'(\*+)?\s*'                                # Optional pointer(s)
        r'([a-zA-Z_][a-zA-Z_0-9]*)'                 # Variable name
    )

    # Pattern for local variable declaration: type var = expr; or type var;
    LOCAL_VAR_PATTERN = re.compile(
        r'^\s*'
        r'((?:unsigned\s+|const\s+|static\s+)*)'   # Optional qualifiers
        r'(char|short|int|long|float|double)\s*'   # Base type
        r'(\*+)?\s*'                                # Optional pointer(s)
        r'([a-zA-Z_][a-zA-Z_0-9]*)\s*'              # Variable name
        r'(?:=\s*[^;]+)?\s*;',                      # Optional init and semicolon
        re.MULTILINE
    )

    NUM_LANES_PATTERN = re.compile(
        r'numLanes\s*\(\s*([0-9]*)\s*\)'
    )

    SCRATCHPAD_OFFSET_PATTERN = re.compile(
        r'scratchpadOffset\s*\(\s*([0-9]*)\s*\)'
    )

    MAX_REQ_IN_FLIGHT_PATTERN = re.compile(
        r'maxRequestsInFlight\s*\(\s*([0-9]*)\s*\)'
    )

    def __init__(self):
        """Initialize the preprocessor."""
        pass

    # -------------------------------------------------------------------------
    # Comment Handling
    # -------------------------------------------------------------------------

    def _strip_comments(self, source: str) -> str:
        """
        Remove C-style comments from source code while preserving line numbers.

        This method handles:
        - Single-line comments: // ... (removes from // to end of line)
        - Multi-line comments: /* ... */ (removes entire block, preserving newlines)

        The method preserves newlines so that line numbers remain accurate for
        error reporting and source location tracking.

        Args:
            source: The source code to process

        Returns:
            Source code with all comments removed, newlines preserved

        Example:
            Input:  "#pragma for // reduction(+, sum)"
            Output: "#pragma for "

            Input:  "/* commented out\n   multi-line */\ncode"
            Output: "                \n              \ncode"
        """
        result = []
        i = 0
        in_string = False
        string_char = None

        while i < len(source):
            # Handle string literals - don't strip comments inside strings
            if not in_string and source[i] in '"\'':
                in_string = True
                string_char = source[i]
                result.append(source[i])
                i += 1
                continue
            elif in_string:
                if source[i] == '\\' and i + 1 < len(source):
                    # Escape sequence - skip both characters
                    result.append(source[i:i+2])
                    i += 2
                    continue
                elif source[i] == string_char:
                    in_string = False
                    string_char = None
                result.append(source[i])
                i += 1
                continue

            # Check for single-line comment //
            if i + 1 < len(source) and source[i:i+2] == '//':
                # Skip until end of line, but keep the newline
                while i < len(source) and source[i] != '\n':
                    result.append(' ')  # Replace with space to preserve positions
                    i += 1
                continue

            # Check for multi-line comment /*
            if i + 1 < len(source) and source[i:i+2] == '/*':
                # Skip until */, preserving newlines
                i += 2
                result.append('  ')  # Replace /* with spaces
                while i < len(source):
                    if i + 1 < len(source) and source[i:i+2] == '*/':
                        result.append('  ')  # Replace */ with spaces
                        i += 2
                        break
                    elif source[i] == '\n':
                        result.append('\n')  # Preserve newlines
                        i += 1
                    else:
                        result.append(' ')  # Replace with space
                        i += 1
                continue

            # Regular character
            result.append(source[i])
            i += 1

        return ''.join(result)

    def _strip_line_comments(self, line: str) -> str:
        """
        Remove single-line comment from a line, handling strings properly.

        Args:
            line: A single line of code

        Returns:
            Line with // comment removed (if not inside a string)
        """
        in_string = False
        string_char = None
        i = 0

        while i < len(line):
            if not in_string and line[i] in '"\'':
                in_string = True
                string_char = line[i]
            elif in_string:
                if line[i] == '\\' and i + 1 < len(line):
                    i += 1  # Skip escape sequence
                elif line[i] == string_char:
                    in_string = False
                    string_char = None
            elif not in_string and i + 1 < len(line) and line[i:i+2] == '//':
                return line[:i]
            i += 1

        return line

    def _is_line_commented(self, line: str) -> bool:
        """
        Check if a line is entirely commented out (starts with //).

        Args:
            line: A single line of code

        Returns:
            True if the line starts with // (after stripping whitespace)
        """
        stripped = line.lstrip()
        return stripped.startswith('//')

    # -------------------------------------------------------------------------
    # Type Context Extraction
    # -------------------------------------------------------------------------

    def _extract_type_context(self, source: str, idiom_start_line: int) -> Dict[str, VariableTypeInfo]:
        """
        Extract type information for variables from surrounding source code.

        This method scans the source code to find type declarations for variables
        that may be used within the idiom block. It looks for:
        - Event parameters (e.g., "event e(long* myArray)")
        - Local variable declarations before the idiom (e.g., "long sum = 0;")

        Args:
            source: The full source code
            idiom_start_line: The line number where the idiom starts

        Returns:
            Dict mapping variable names to their VariableTypeInfo
        """
        type_context: Dict[str, VariableTypeInfo] = {}

        # Split source into lines for line-based processing
        lines = source.split('\n')
        source_before_idiom = '\n'.join(lines[:idiom_start_line])

        # Find the enclosing event declaration
        # Search backwards from the idiom for the most recent event declaration
        event_matches = list(self.EVENT_DECL_PATTERN.finditer(source_before_idiom))
        if event_matches:
            # Use the last (most recent) event declaration
            last_event = event_matches[-1]
            event_name = last_event.group(1)
            params_str = last_event.group(2)

            # Parse each parameter
            for param_match in self.PARAM_DECL_PATTERN.finditer(params_str):
                qualifiers_str = param_match.group(1).strip()
                base_type = param_match.group(2)
                pointer_str = param_match.group(3) or ''
                var_name = param_match.group(4)

                qualifiers = qualifiers_str.split() if qualifiers_str else []
                pointer_depth = len(pointer_str)

                type_info = VariableTypeInfo(
                    var_name=var_name,
                    base_type=base_type,
                    qualifiers=qualifiers,
                    is_pointer=pointer_depth > 0,
                    pointer_depth=pointer_depth,
                    source='event_param'
                )
                type_context[var_name] = type_info

        # Find local variable declarations between event start and idiom
        # We need to find where the last event body starts
        if event_matches:
            event_body_start = event_matches[-1].end()
            local_scope = source_before_idiom[event_body_start:]

            for var_match in self.LOCAL_VAR_PATTERN.finditer(local_scope):
                qualifiers_str = var_match.group(1).strip()
                base_type = var_match.group(2)
                pointer_str = var_match.group(3) or ''
                var_name = var_match.group(4)

                qualifiers = qualifiers_str.split() if qualifiers_str else []
                pointer_depth = len(pointer_str)

                type_info = VariableTypeInfo(
                    var_name=var_name,
                    base_type=base_type,
                    qualifiers=qualifiers,
                    is_pointer=pointer_depth > 0,
                    pointer_depth=pointer_depth,
                    source='local_var'
                )
                type_context[var_name] = type_info

        return type_context

    def _apply_type_context_to_stores(self, idiom: IdiomConstruct) -> None:
        """
        Apply type context information to store operations.

        This updates each StoreOperation with type information from the
        idiom's type_context, if available.

        Args:
            idiom: The IdiomConstruct to update
        """
        for store in idiom.store_operations:
            if store.array_name in idiom.type_context:
                store.array_type = idiom.type_context[store.array_name]

    # -------------------------------------------------------------------------
    # Brace Matching Utilities
    # -------------------------------------------------------------------------

    def _find_matching_brace(self, source: str, start: int) -> int:
        """
        Find the position of the closing brace that matches the opening brace at start.

        This properly handles:
        - Nested braces at any depth
        - String literals (won't count braces inside "...")
        - Character literals (won't count braces inside '...')
        - Single-line comments (// ...)
        - Multi-line comments (/* ... */)

        Args:
            source: The source string to search
            start: Position of the opening brace '{'

        Returns:
            Position of the matching closing brace '}', or -1 if not found
        """
        if start >= len(source) or source[start] != '{':
            return -1

        depth = 0
        i = start
        in_string = False
        in_char = False
        in_comment = False
        in_multiline_comment = False

        while i < len(source):
            c = source[i]

            # Handle escape sequences in strings/chars (skip the escaped character)
            if (in_string or in_char) and c == '\\' and i + 1 < len(source):
                i += 2  # Skip the escape sequence
                continue

            # Toggle string literal state on unescaped quote
            if c == '"' and not in_char and not in_comment and not in_multiline_comment:
                in_string = not in_string

            # Toggle char literal state on unescaped single quote
            elif c == "'" and not in_string and not in_comment and not in_multiline_comment:
                in_char = not in_char

            # Start of single-line comment
            elif c == '/' and i + 1 < len(source) and source[i+1] == '/' and \
                    not in_string and not in_char and not in_multiline_comment:
                in_comment = True
                i += 1

            # Start of multi-line comment
            elif c == '/' and i + 1 < len(source) and source[i+1] == '*' and \
                    not in_string and not in_char and not in_comment:
                in_multiline_comment = True
                i += 1

            # End of multi-line comment
            elif c == '*' and i + 1 < len(source) and source[i+1] == '/' and in_multiline_comment:
                in_multiline_comment = False
                i += 1

            # Newline ends single-line comment
            elif c == '\n' and in_comment:
                in_comment = False

            # Count braces only when not inside strings, chars, or comments
            elif not in_string and not in_char and not in_comment and not in_multiline_comment:
                if c == '{':
                    depth += 1
                elif c == '}':
                    depth -= 1
                    if depth == 0:
                        return i

            i += 1

        return -1  # No matching brace found

    def _find_matching_paren(self, source: str, start: int) -> int:
        """
        Find the position of the closing parenthesis that matches the opening one at start.

        Similar to _find_matching_brace but for parentheses.

        Args:
            source: The source string to search
            start: Position of the opening parenthesis '('

        Returns:
            Position of the matching closing parenthesis ')', or -1 if not found
        """
        if start >= len(source) or source[start] != '(':
            return -1

        depth = 0
        i = start
        in_string = False
        in_char = False

        while i < len(source):
            c = source[i]

            # Handle escape sequences
            if (in_string or in_char) and c == '\\' and i + 1 < len(source):
                i += 2
                continue

            if c == '"' and not in_char:
                in_string = not in_string
            elif c == "'" and not in_string:
                in_char = not in_char
            elif not in_string and not in_char:
                if c == '(':
                    depth += 1
                elif c == ')':
                    depth -= 1
                    if depth == 0:
                        return i

            i += 1

        return -1

    # -------------------------------------------------------------------------
    # Block Content Extraction
    # -------------------------------------------------------------------------

    def _extract_block_content(self, source: str, keyword: str, start_search: int = 0) -> Tuple[str, int, int]:
        """
        Extract the content of a named block (Let or In) from the source.

        Searches for pattern: keyword { ... } and extracts the content between braces.

        Args:
            source: The source string
            keyword: The keyword to look for ('Let' or 'In')
            start_search: Position to start searching from

        Returns:
            Tuple of (block_content, block_start_pos, block_end_pos)
            block_content: Text inside the braces (excluding braces)
            block_start_pos: Position where keyword starts
            block_end_pos: Position after closing brace
            Returns ("", -1, -1) if block not found
        """
        # Find the keyword followed by opening brace
        pattern = re.compile(rf'\b{keyword}\s*\{{', re.DOTALL)
        match = pattern.search(source, start_search)
        if not match:
            return "", -1, -1

        # Find the matching closing brace
        brace_start = match.end() - 1  # Position of '{'
        brace_end = self._find_matching_brace(source, brace_start)

        if brace_end == -1:
            return "", -1, -1

        # Extract content between braces (excluding the braces themselves)
        content = source[brace_start + 1:brace_end]

        return content, match.start(), brace_end + 1

    # -------------------------------------------------------------------------
    # Component Parsing Methods
    # -------------------------------------------------------------------------

    def _parse_let_declarations(self, let_content: str, loop_var: Optional[str] = None) -> List[LetDeclaration]:
        """
        Parse variable declarations from Let block content.

        Each declaration in the Let block should have the form:
            type [qualifiers] [*[local]] varname = expression;

        Examples:
            long a = myArray[16];
            unsigned long b = data[i];
            int *ptr = baseAddr;
            float *local scratch = LMBASE;

        Args:
            let_content: The raw content inside the Let { } block
            loop_var: The loop variable name (for classifying array indices)

        Returns:
            List of LetDeclaration objects in declaration order
        """
        declarations = []

        for match in self.LET_DECL_PATTERN.finditer(let_content):
            qualifiers_str = match.group(1).strip()
            base_type = match.group(2)
            pointer_spec = match.group(3) or ""
            var_name = match.group(4)
            expr = match.group(5).strip()

            # Parse qualifiers (split on whitespace)
            qualifiers = qualifiers_str.split() if qualifiers_str else []

            # Determine pointer type from pointer specifier
            is_pointer = '*' in pointer_spec
            is_local_pointer = 'local' in pointer_spec.lower()

            # Parse the source expression if it's an array access
            parsed_source = self._parse_array_access(expr, loop_var)

            decl = LetDeclaration(
                var_type=base_type,
                var_name=var_name,
                source_expr=expr,
                parsed_source=parsed_source,
                is_pointer=is_pointer,
                is_local_pointer=is_local_pointer,
                qualifiers=qualifiers,
                raw_declaration=match.group(0).strip()
            )
            declarations.append(decl)

        return declarations

    def _parse_reductions(self, idiom_text: str) -> List[ReductionSpec]:
        """
        Parse all reduction clauses from pragma text.

        Multiple reductions are allowed in a single pragma.
        Reduction syntax: reduction(operator, variable)
        Where operator is one of: +, -, *, /, &, |, ^

        Args:
            idiom_text: The pragma text to search

        Returns:
            List of ReductionSpec objects (empty list if none found)
        """
        reductions = []
        for match in self.REDUCTION_PATTERN.finditer(idiom_text):
            reductions.append(ReductionSpec(operator=match.group(1), variable=match.group(2)))
        return reductions

    def _parse_num_lanes(self, idiom_text: str) -> Optional[int]:
        """
        Parse numLanes clause from pragma text.

        numLanes syntax: numLanes(value)

        Args:
            idiom_text: The pragma text to search

        Returns:
            Integer value if found, None otherwise
        """
        match = self.NUM_LANES_PATTERN.search(idiom_text)
        if match:
            return int(match.group(1))
        return None

    def _parse_scratchpad_offset(self, idiom_text: str) -> Optional[str]:
        """
        Parse scratchpadOffset clause from pragma text.

        scratchpadOffset syntax: scratchpadOffset(value)

        Args:
            idiom_text: The pragma text to search

        Returns:
            String value if found, None otherwise
        """
        match = self.SCRATCHPAD_OFFSET_PATTERN.search(idiom_text)
        if match:
            return match.group(1)
        return None

    def _parse_max_requests_in_flight(self, idiom_text: str) -> Optional[int]:
        """
        Parse maxRequestsInFlight clause from pragma text.

        maxRequestsInFlight syntax: maxRequestsInFlight(value)

        Args:
            idiom_text: The pragma text to search

        Returns:
            Integer value if found, None otherwise
        """
        match = self.MAX_REQ_IN_FLIGHT_PATTERN.search(idiom_text)
        if match:
            return int(match.group(1))
        return None

    def _parse_oncomplete(self, idiom_text: str) -> Optional[OnCompleteSpec]:
        """
        Parse onComplete clause from pragma text.

        onComplete syntax: onComplete(eventName [, arg1, arg2, ...])
        Event name can include namespace: thread::event or thread::ns::event

        Args:
            idiom_text: The pragma text to search

        Returns:
            OnCompleteSpec if found, None otherwise
        """
        match = self.ONCOMPLETE_PATTERN.search(idiom_text)
        if match:
            event_name = match.group(1)
            args_str = match.group(2)
            arguments = []
            if args_str:
                # Split arguments by comma and strip whitespace from each
                arguments = [arg.strip() for arg in args_str.split(',') if arg.strip()]
            return OnCompleteSpec(event_name=event_name, arguments=arguments)
        return None

    def _parse_index_expr(self, index_str: str, loop_var: Optional[str] = None) -> IndexExpr:
        """
        Parse an array index expression and classify it.

        Classifies the index as:
        - CONSTANT: A literal integer value (e.g., 16, 0x10, 0b1010)
        - LOOP_VAR: The loop iteration variable (if it matches loop_var parameter)
        - VARIABLE: A simple identifier that is not the loop variable
        - EXPRESSION: A complex expression (e.g., 'i + 1', 'offset * 2')

        Args:
            index_str: The raw index expression string
            loop_var: The loop variable name (if inside a for loop)

        Returns:
            IndexExpr with classification and parsed details
        """
        index_str = index_str.strip()

        # Check if it's an integer constant
        const_match = self.INTEGER_CONSTANT_PATTERN.match(index_str)
        if const_match:
            # Parse the constant value
            val_str = const_match.group(1)
            if val_str.startswith('0x'):
                value = int(val_str, 16)
            elif val_str.startswith('0b'):
                value = int(val_str, 2)
            elif val_str.startswith('0') and len(val_str) > 1:
                value = int(val_str, 8)
            else:
                value = int(val_str)
            return IndexExpr(
                raw_expr=index_str,
                index_type=IndexType.CONSTANT,
                constant_value=value
            )

        # Check if it's a simple identifier
        id_match = self.IDENTIFIER_PATTERN.match(index_str)
        if id_match:
            var_name = id_match.group(1)
            # Check if it's the loop variable
            if loop_var and var_name == loop_var:
                return IndexExpr(
                    raw_expr=index_str,
                    index_type=IndexType.LOOP_VAR,
                    base_variable=var_name,
                    involves_loop_var=True
                )
            else:
                return IndexExpr(
                    raw_expr=index_str,
                    index_type=IndexType.VARIABLE,
                    base_variable=var_name
                )

        # It's a complex expression - check if it involves the loop variable
        involves_loop = False
        if loop_var:
            # Check if loop_var appears as a whole word in the expression
            if re.search(rf'\b{re.escape(loop_var)}\b', index_str):
                involves_loop = True

        return IndexExpr(
            raw_expr=index_str,
            index_type=IndexType.EXPRESSION,
            involves_loop_var=involves_loop
        )

    def _parse_array_access(self, expr: str, loop_var: Optional[str] = None) -> Optional[ArrayAccessExpr]:
        """
        Parse an array access expression like myArray[i] or data[16].

        Args:
            expr: The expression to parse
            loop_var: The loop variable name (if inside a for loop)

        Returns:
            ArrayAccessExpr if the expression is an array access, None otherwise
        """
        match = self.ARRAY_ACCESS_PATTERN.match(expr.strip())
        if not match:
            return None

        array_name = match.group(1)
        index_str = match.group(2).strip()

        # Parse the index expression
        index_expr = self._parse_index_expr(index_str, loop_var)

        return ArrayAccessExpr(
            array_name=array_name,
            index=index_expr,
            raw_expr=expr.strip()
        )

    def _parse_store_operations(self, in_body: str, let_var_names: List[str],
                                 loop_var: Optional[str] = None) -> List[StoreOperation]:
        """
        Parse store operations from the In block.

        Identifies statements like "myArrayB[i] = a;" and extracts:
        - The target array and index
        - The value expression
        - Which Let variables are used in the value

        Args:
            in_body: The raw content of the In block
            let_var_names: List of variable names declared in the Let block
            loop_var: The loop variable name (if inside a for loop)

        Returns:
            List of StoreOperation objects found in the In block
        """
        stores = []

        for match in self.ARRAY_STORE_PATTERN.finditer(in_body):
            array_name = match.group(1)
            index_str = match.group(2).strip()
            value_expr = match.group(3).strip()

            # Parse the index expression
            index_expr = self._parse_index_expr(index_str, loop_var)

            # Find which Let variables are used in the value expression
            source_let_vars = []
            for let_var in let_var_names:
                # Check if the Let variable appears as a whole word in the value expression
                if re.search(rf'\b{re.escape(let_var)}\b', value_expr):
                    source_let_vars.append(let_var)

            store = StoreOperation(
                array_name=array_name,
                index=index_expr,
                value_expr=value_expr,
                source_let_vars=source_let_vars,
                raw_statement=match.group(0).strip()
            )
            stores.append(store)

        return stores

    # -------------------------------------------------------------------------
    # In-Block Expression Parsing (for unrolling support)
    # -------------------------------------------------------------------------

    def _tokenize_expression(self, expr: str) -> List[Tuple[str, str]]:
        """
        Tokenize an expression string into tokens.

        Returns list of (token_type, token_value) tuples.
        Token types: 'NUMBER', 'IDENT', 'OP', 'LPAREN', 'RPAREN', 'COMMA'
        """
        tokens = []
        i = 0
        expr = expr.strip()

        while i < len(expr):
            # Skip whitespace
            if expr[i].isspace():
                i += 1
                continue

            # Numbers (int or float)
            if expr[i].isdigit() or (expr[i] == '.' and i + 1 < len(expr) and expr[i + 1].isdigit()):
                j = i
                while j < len(expr) and (expr[j].isdigit() or expr[j] == '.' or expr[j] in 'xXabcdefABCDEF'):
                    j += 1
                tokens.append(('NUMBER', expr[i:j]))
                i = j
                continue

            # Identifiers
            if expr[i].isalpha() or expr[i] == '_':
                j = i
                while j < len(expr) and (expr[j].isalnum() or expr[j] == '_'):
                    j += 1
                tokens.append(('IDENT', expr[i:j]))
                i = j
                continue

            # Multi-character operators
            if i + 1 < len(expr):
                two_char = expr[i:i + 2]
                if two_char in ('<=', '>=', '==', '!=', '&&', '||', '<<', '>>', '+=', '-=', '*=', '/=', '%=', '&=', '|=', '^='):
                    tokens.append(('OP', two_char))
                    i += 2
                    continue

            # Single character operators and punctuation
            if expr[i] in '+-*/%&|^<>!=~':
                tokens.append(('OP', expr[i]))
                i += 1
                continue

            if expr[i] == '(':
                tokens.append(('LPAREN', '('))
                i += 1
                continue

            if expr[i] == ')':
                tokens.append(('RPAREN', ')'))
                i += 1
                continue

            if expr[i] == ',':
                tokens.append(('COMMA', ','))
                i += 1
                continue

            if expr[i] == ';':
                i += 1
                continue

            # Skip unknown characters
            i += 1

        return tokens

    def _parse_expression_tokens(self, tokens: List[Tuple[str, str]], pos: int,
                                  let_vars: set, reduction_vars: set,
                                  loop_var: Optional[str]) -> Tuple[Optional[InBlockExpr], int]:
        """
        Parse tokens into an expression tree using recursive descent.
        Returns (expression, new_position).
        """
        return self._parse_additive(tokens, pos, let_vars, reduction_vars, loop_var)

    def _parse_additive(self, tokens: List[Tuple[str, str]], pos: int,
                        let_vars: set, reduction_vars: set,
                        loop_var: Optional[str]) -> Tuple[Optional[InBlockExpr], int]:
        """Parse additive expressions (+ -)."""
        left, pos = self._parse_multiplicative(tokens, pos, let_vars, reduction_vars, loop_var)
        if left is None:
            return None, pos

        while pos < len(tokens) and tokens[pos][0] == 'OP' and tokens[pos][1] in ('+', '-'):
            op_str = tokens[pos][1]
            op = BinaryOp.ADD if op_str == '+' else BinaryOp.SUB
            pos += 1
            right, pos = self._parse_multiplicative(tokens, pos, let_vars, reduction_vars, loop_var)
            if right is None:
                break
            left = InBlockExpr(
                expr_type=ExprType.BINARY_OP,
                binary_op=op,
                left=left,
                right=right
            )

        return left, pos

    def _parse_multiplicative(self, tokens: List[Tuple[str, str]], pos: int,
                               let_vars: set, reduction_vars: set,
                               loop_var: Optional[str]) -> Tuple[Optional[InBlockExpr], int]:
        """Parse multiplicative expressions (* / %)."""
        left, pos = self._parse_unary(tokens, pos, let_vars, reduction_vars, loop_var)
        if left is None:
            return None, pos

        while pos < len(tokens) and tokens[pos][0] == 'OP' and tokens[pos][1] in ('*', '/', '%'):
            op_str = tokens[pos][1]
            if op_str == '*':
                op = BinaryOp.MUL
            elif op_str == '/':
                op = BinaryOp.DIV
            else:
                op = BinaryOp.MOD
            pos += 1
            right, pos = self._parse_unary(tokens, pos, let_vars, reduction_vars, loop_var)
            if right is None:
                break
            left = InBlockExpr(
                expr_type=ExprType.BINARY_OP,
                binary_op=op,
                left=left,
                right=right
            )

        return left, pos

    def _parse_unary(self, tokens: List[Tuple[str, str]], pos: int,
                     let_vars: set, reduction_vars: set,
                     loop_var: Optional[str]) -> Tuple[Optional[InBlockExpr], int]:
        """Parse unary expressions (- ! ~)."""
        if pos < len(tokens) and tokens[pos][0] == 'OP' and tokens[pos][1] in ('-', '!', '~'):
            op_str = tokens[pos][1]
            if op_str == '-':
                op = UnaryOp.NEG
            elif op_str == '!':
                op = UnaryOp.NOT
            else:
                op = UnaryOp.BITNOT
            pos += 1
            operand, pos = self._parse_unary(tokens, pos, let_vars, reduction_vars, loop_var)
            if operand:
                return InBlockExpr(
                    expr_type=ExprType.UNARY_OP,
                    unary_op=op,
                    operand=operand
                ), pos
            return None, pos

        return self._parse_primary(tokens, pos, let_vars, reduction_vars, loop_var)

    def _parse_primary(self, tokens: List[Tuple[str, str]], pos: int,
                       let_vars: set, reduction_vars: set,
                       loop_var: Optional[str]) -> Tuple[Optional[InBlockExpr], int]:
        """Parse primary expressions (numbers, identifiers, parenthesized)."""
        if pos >= len(tokens):
            return None, pos

        token_type, token_value = tokens[pos]

        # Number literal
        if token_type == 'NUMBER':
            try:
                if '.' in token_value:
                    val = float(token_value)
                    const_type = 'float'
                elif token_value.startswith('0x') or token_value.startswith('0X'):
                    val = int(token_value, 16)
                    const_type = 'int'
                else:
                    val = int(token_value)
                    const_type = 'int'
            except ValueError:
                val = token_value
                const_type = 'unknown'

            return InBlockExpr(
                expr_type=ExprType.CONSTANT,
                constant_value=val,
                constant_type=const_type,
                raw_text=token_value
            ), pos + 1

        # Identifier (variable)
        if token_type == 'IDENT':
            var_name = token_value
            var_info = VariableInfo(
                name=var_name,
                is_let_var=var_name in let_vars,
                is_reduction_var=var_name in reduction_vars,
                is_loop_var=(var_name == loop_var) if loop_var else False
            )
            return InBlockExpr(
                expr_type=ExprType.VARIABLE,
                var_info=var_info,
                raw_text=var_name
            ), pos + 1

        # Parenthesized expression
        if token_type == 'LPAREN':
            pos += 1
            expr, pos = self._parse_expression_tokens(tokens, pos, let_vars, reduction_vars, loop_var)
            if pos < len(tokens) and tokens[pos][0] == 'RPAREN':
                pos += 1
            return expr, pos

        return None, pos

    def _parse_in_block_statement(self, stmt: str, let_vars: set, reduction_vars: set,
                                   loop_var: Optional[str]) -> Optional[InBlockStatement]:
        """
        Parse a single In-block statement into structured form.

        Handles:
        - Simple assignments: x = expr;
        - Compound assignments: x += expr; x *= expr;
        - Array stores: arr[i] = expr; (handled separately)

        Args:
            stmt: The statement string
            let_vars: Set of Let variable names
            reduction_vars: Set of reduction variable names
            loop_var: Loop variable name if in a loop

        Returns:
            InBlockStatement or None if parsing fails
        """
        stmt = stmt.strip()
        if not stmt or stmt == ';':
            return None

        # Check for compound assignment operators
        compound_ops = ['+=', '-=', '*=', '/=', '%=', '&=', '|=', '^=']
        assignment_type = AssignmentType.SIMPLE
        split_pos = -1

        for op in compound_ops:
            pos = stmt.find(op)
            if pos != -1:
                if op == '+=':
                    assignment_type = AssignmentType.ADD_ASSIGN
                elif op == '-=':
                    assignment_type = AssignmentType.SUB_ASSIGN
                elif op == '*=':
                    assignment_type = AssignmentType.MUL_ASSIGN
                elif op == '/=':
                    assignment_type = AssignmentType.DIV_ASSIGN
                elif op == '%=':
                    assignment_type = AssignmentType.MOD_ASSIGN
                elif op == '&=':
                    assignment_type = AssignmentType.AND_ASSIGN
                elif op == '|=':
                    assignment_type = AssignmentType.OR_ASSIGN
                elif op == '^=':
                    assignment_type = AssignmentType.XOR_ASSIGN
                split_pos = pos
                break

        # Check for simple assignment (but not ==, !=, <=, >=)
        if split_pos == -1:
            for i, c in enumerate(stmt):
                if c == '=' and i > 0:
                    prev = stmt[i - 1] if i > 0 else ''
                    next_c = stmt[i + 1] if i + 1 < len(stmt) else ''
                    if prev not in '!<>=' and next_c != '=':
                        split_pos = i
                        break

        if split_pos == -1:
            return None

        # Extract LHS and RHS
        op_len = 2 if assignment_type != AssignmentType.SIMPLE else 1
        lhs = stmt[:split_pos].strip()
        rhs = stmt[split_pos + op_len:].strip().rstrip(';')

        # Check if LHS is an array access (handled by store operations)
        if '[' in lhs:
            return None  # Skip array stores, handled separately

        # Parse the RHS expression
        tokens = self._tokenize_expression(rhs)
        value_expr, _ = self._parse_expression_tokens(tokens, 0, let_vars, reduction_vars, loop_var)

        return InBlockStatement(
            target_var=lhs,
            assignment_type=assignment_type,
            value_expr=value_expr,
            raw_statement=stmt
        )

    def _parse_in_block(self, in_body: str, let_declarations: List[LetDeclaration],
                        reduction_vars: List[str], loop_var: Optional[str]) -> ParsedInBlock:
        """
        Parse the entire In-block into structured form.

        Args:
            in_body: Raw In-block content
            let_declarations: List of Let declarations for context
            reduction_vars: List of reduction variable names
            loop_var: Loop variable name if present

        Returns:
            ParsedInBlock with all parsed statements
        """
        let_vars = {decl.var_name for decl in let_declarations}
        reduction_set = set(reduction_vars)

        # Create let var mapping
        let_var_mapping = {decl.var_name: decl for decl in let_declarations}

        # Split into statements
        statements = []
        # Simple split by semicolon (doesn't handle all edge cases but works for basic expressions)
        raw_statements = [s.strip() for s in in_body.split(';') if s.strip()]

        for raw_stmt in raw_statements:
            parsed = self._parse_in_block_statement(raw_stmt + ';', let_vars, reduction_set, loop_var)
            if parsed:
                # Link Let declarations to variable infos
                if parsed.value_expr:
                    for var_info in parsed.value_expr.get_all_variables():
                        if var_info.is_let_var and var_info.name in let_var_mapping:
                            var_info.let_decl = let_var_mapping[var_info.name]
                statements.append(parsed)

        return ParsedInBlock(
            statements=statements,
            raw_content=in_body,
            let_var_mapping=let_var_mapping,
            reduction_vars=reduction_set
        )

    def _parse_loop_bound(self, expr: str) -> LoopBound:
        """
        Parse a loop bound expression (start or end value).

        Handles:
        - Integer literals: 0, 100, 0x10, 0b1010
        - Variables/macros: LIMIT, size, n
        - Simple expressions: n-1, size/2

        Args:
            expr: The expression string to parse

        Returns:
            LoopBound with parsed information
        """
        expr = expr.strip()

        # Try to parse as integer literal
        # Decimal
        if re.match(r'^-?\d+$', expr):
            return LoopBound(
                raw_expr=expr,
                is_constant=True,
                constant_value=int(expr)
            )

        # Hexadecimal
        if re.match(r'^0[xX][0-9a-fA-F]+$', expr):
            return LoopBound(
                raw_expr=expr,
                is_constant=True,
                constant_value=int(expr, 16)
            )

        # Binary
        if re.match(r'^0[bB][01]+$', expr):
            return LoopBound(
                raw_expr=expr,
                is_constant=True,
                constant_value=int(expr, 2)
            )

        # Octal
        if re.match(r'^0[0-7]+$', expr):
            return LoopBound(
                raw_expr=expr,
                is_constant=True,
                constant_value=int(expr, 8)
            )

        # Check if it's a simple identifier (variable or macro)
        if re.match(r'^[a-zA-Z_][a-zA-Z_0-9]*$', expr):
            return LoopBound(
                raw_expr=expr,
                is_constant=False,
                variable_name=expr
            )

        # It's a more complex expression
        return LoopBound(
            raw_expr=expr,
            is_constant=False
        )

    def _parse_loop_condition(self, condition: str, loop_var: str) -> Tuple[Optional[LoopBound], str]:
        """
        Parse a loop condition to extract the end bound and comparison operator.

        Handles conditions like:
        - i < LIMIT
        - i <= n-1
        - i != end
        - LIMIT > i (reversed)

        Args:
            condition: The condition expression string
            loop_var: The loop variable name

        Returns:
            Tuple of (LoopBound for end value, comparison operator string)
        """
        condition = condition.strip()

        # Patterns for different comparison operators
        # Format: var op expr  or  expr op var
        comparison_ops = ['<=', '>=', '<', '>', '!=']

        for op in comparison_ops:
            if op in condition:
                parts = condition.split(op, 1)
                if len(parts) == 2:
                    left = parts[0].strip()
                    right = parts[1].strip()

                    # Check which side has the loop variable
                    if left == loop_var:
                        # Normal form: i < LIMIT
                        end_bound = self._parse_loop_bound(right)
                        return end_bound, op
                    elif right == loop_var:
                        # Reversed form: LIMIT > i
                        end_bound = self._parse_loop_bound(left)
                        # Flip the operator
                        flipped_ops = {'<': '>', '>': '<', '<=': '>=', '>=': '<=', '!=': '!='}
                        return end_bound, flipped_ops.get(op, op)

        # Could not parse condition
        return LoopBound(raw_expr=condition), '?'

    def _parse_loop_stride(self, increment: str, loop_var: str) -> LoopStride:
        """
        Parse a loop increment expression to extract the stride.

        Handles:
        - i++, ++i → stride = 1
        - i--, --i → stride = -1
        - i += N → stride = N
        - i -= N → stride = -N
        - i = i + N → stride = N
        - i = i - N → stride = -N

        Args:
            increment: The increment expression string
            loop_var: The loop variable name

        Returns:
            LoopStride with parsed information
        """
        increment = increment.strip()
        var_pattern = re.escape(loop_var)

        # i++ or ++i
        if re.match(rf'^{var_pattern}\s*\+\+$', increment) or re.match(rf'^\+\+\s*{var_pattern}$', increment):
            return LoopStride(
                raw_expr=increment,
                is_constant=True,
                constant_value=1,
                direction=1
            )

        # i-- or --i
        if re.match(rf'^{var_pattern}\s*--$', increment) or re.match(rf'^--\s*{var_pattern}$', increment):
            return LoopStride(
                raw_expr=increment,
                is_constant=True,
                constant_value=-1,
                direction=-1
            )

        # i += expr
        match = re.match(rf'^{var_pattern}\s*\+=\s*(.+)$', increment)
        if match:
            stride_expr = match.group(1).strip()
            bound = self._parse_loop_bound(stride_expr)
            if bound.is_constant:
                return LoopStride(
                    raw_expr=increment,
                    is_constant=True,
                    constant_value=bound.constant_value,
                    direction=1 if bound.constant_value > 0 else -1
                )
            else:
                return LoopStride(
                    raw_expr=increment,
                    is_constant=False,
                    variable_name=bound.variable_name,
                    direction=1  # Assume positive for variables
                )

        # i -= expr
        match = re.match(rf'^{var_pattern}\s*-=\s*(.+)$', increment)
        if match:
            stride_expr = match.group(1).strip()
            bound = self._parse_loop_bound(stride_expr)
            if bound.is_constant:
                return LoopStride(
                    raw_expr=increment,
                    is_constant=True,
                    constant_value=-bound.constant_value,
                    direction=-1 if bound.constant_value > 0 else 1
                )
            else:
                return LoopStride(
                    raw_expr=increment,
                    is_constant=False,
                    variable_name=bound.variable_name,
                    direction=-1  # Assume negative direction
                )

        # i = i + expr or i = i - expr
        match = re.match(rf'^{var_pattern}\s*=\s*{var_pattern}\s*([+\-])\s*(.+)$', increment)
        if match:
            op = match.group(1)
            stride_expr = match.group(2).strip()
            bound = self._parse_loop_bound(stride_expr)

            if op == '+':
                if bound.is_constant:
                    return LoopStride(
                        raw_expr=increment,
                        is_constant=True,
                        constant_value=bound.constant_value,
                        direction=1 if bound.constant_value > 0 else -1
                    )
                else:
                    return LoopStride(
                        raw_expr=increment,
                        is_constant=False,
                        variable_name=bound.variable_name,
                        direction=1
                    )
            else:  # op == '-'
                if bound.is_constant:
                    return LoopStride(
                        raw_expr=increment,
                        is_constant=True,
                        constant_value=-bound.constant_value,
                        direction=-1 if bound.constant_value > 0 else 1
                    )
                else:
                    return LoopStride(
                        raw_expr=increment,
                        is_constant=False,
                        variable_name=bound.variable_name,
                        direction=-1
                    )

        # Could not parse - return unknown stride
        return LoopStride(
            raw_expr=increment,
            is_constant=False,
            direction=0
        )

    def _parse_for_loop(self, source: str, start_pos: int) -> Tuple[Optional[ForLoopSpec], int, int]:
        """
        Parse a for loop header starting from the given position.

        Searches for a for loop and extracts its components:
        - Variable type and qualifiers
        - Variable name
        - Initialization value
        - Loop condition
        - Increment expression

        Args:
            source: The source string
            start_pos: Position to start searching for the for loop

        Returns:
            Tuple of (ForLoopSpec, loop_body_start, loop_body_end)
            - ForLoopSpec: Parsed loop specification (None if no for loop found)
            - loop_body_start: Position of opening brace of loop body
            - loop_body_end: Position after closing brace of loop body
        """
        # Search for 'for' keyword after the pragma
        for_match = re.search(r'\bfor\s*\(', source[start_pos:])
        if not for_match:
            return None, -1, -1

        for_start = start_pos + for_match.start()

        # Find the opening parenthesis of the for header
        paren_start = source.find('(', for_start)
        if paren_start == -1:
            return None, -1, -1

        # Find the matching closing parenthesis
        paren_end = self._find_matching_paren(source, paren_start)
        if paren_end == -1:
            return None, -1, -1

        # Extract and parse the for header
        for_header = source[paren_start + 1:paren_end]

        # Parse the for loop header components
        header_match = self.FOR_LOOP_PATTERN.match(source[for_start:])
        if not header_match:
            return None, -1, -1

        qualifiers_str = header_match.group(1).strip()
        var_type = header_match.group(2)
        var_name = header_match.group(3)
        raw_init = header_match.group(4).strip()
        raw_condition = header_match.group(5).strip()
        raw_increment = header_match.group(6).strip()

        qualifiers = qualifiers_str.split() if qualifiers_str else []

        # Parse structured loop information
        start_bound = self._parse_loop_bound(raw_init)
        end_bound, comparison_op = self._parse_loop_condition(raw_condition, var_name)
        stride = self._parse_loop_stride(raw_increment, var_name)

        loop_spec = ForLoopSpec(
            var_type=var_type,
            var_qualifiers=qualifiers,
            var_name=var_name,
            raw_init=raw_init,
            raw_condition=raw_condition,
            raw_increment=raw_increment,
            raw_header=source[for_start:paren_end + 1],
            start=start_bound,
            end=end_bound,
            comparison_op=comparison_op,
            stride=stride
        )

        # Find the loop body (the { } after the for header)
        # Skip whitespace after the closing parenthesis
        body_search_start = paren_end + 1
        brace_match = re.search(r'\{', source[body_search_start:])
        if not brace_match:
            return loop_spec, -1, -1

        body_start = body_search_start + brace_match.start()
        body_end = self._find_matching_brace(source, body_start)

        if body_end == -1:
            return loop_spec, -1, -1

        return loop_spec, body_start, body_end + 1

    # -------------------------------------------------------------------------
    # Pragma Block Finding
    # -------------------------------------------------------------------------

    def find_idiom_blocks(self, source: str) -> List[Tuple[int, int, str]]:
        """
        Find all #pragma blocks with for/reduction/onComplete clauses.

        Clauses can appear in any order after #pragma:
        - for: Indicates a for loop follows (at most 1)
        - reduction(op, var): Reduction specification (multiple allowed)
        - onComplete(event, args...): Completion callback (at most 1)

        Examples of valid pragma lines:
        - #pragma for reduction(+, sum) onComplete(done, sum)
        - #pragma onComplete(done, x) reduction(*, product) for
        - #pragma reduction(+, sum) reduction(*, prod) onComplete(done)
        - #pragma onComplete(done) (no for loop, no reduction)

        The method properly handles:
        - Nested braces at any depth
        - Comments and string literals
        - Multiple idioms in the same file

        Args:
            source: The UDweave source code

        Returns:
            List of tuples: (start_pos, end_pos, idiom_text)
            - start_pos: Character position where pragma starts
            - end_pos: Character position after pragma ends
            - idiom_text: The complete pragma text including all blocks
        """
        blocks = []

        # First, create a version of source with comments stripped for finding pragmas
        # But we keep the original source for position tracking
        source_no_comments = self._strip_comments(source)

        # Pattern to find #pragma followed by any of our recognized clauses
        # We look for #pragma then check if it contains for, reduction, or onComplete
        idiom_start_pattern = re.compile(r'#pragma\s+')

        for match in idiom_start_pattern.finditer(source_no_comments):
            start_pos = match.start()
            search_start = match.end()

            # Find the start of the line containing #pragma
            line_start = source_no_comments.rfind('\n', 0, start_pos)
            line_start = 0 if line_start == -1 else line_start + 1

            # Check if there's a // before #pragma on this line (in original source)
            # This catches cases where the comment stripping left whitespace but we
            # want to verify the original wasn't commented
            line_before_pragma = source[line_start:start_pos]
            if '//' in line_before_pragma:
                # The #pragma is commented out in the original source, skip it
                continue

            # Find the end of the pragma clause line (up to 'Let' keyword or 'for(' loop)
            # We need to extract the full pragma clause to determine if 'for' is present
            # Look ahead to find either 'Let' (no loop) or 'for(' (loop start)
            idiom_line_end = source_no_comments.find('\n', search_start)
            if idiom_line_end == -1:
                idiom_line_end = len(source_no_comments)

            # Get the pragma clauses (between #pragma and newline or Let/for loop)
            # Use the comment-stripped version so inline comments are ignored
            idiom_clauses = source_no_comments[search_start:idiom_line_end]

            # Check if this is a pragma we care about (has for, reduction, or onComplete)
            has_for_clause = bool(re.search(r'\bfor\b(?!\s*\()', idiom_clauses))  # 'for' not followed by '('
            has_reduction = bool(re.search(r'\breduction\s*\(', idiom_clauses))
            has_oncomplete = bool(re.search(r'\bonComplete\s*\(', idiom_clauses))

            if not (has_for_clause or has_reduction or has_oncomplete):
                # Not a pragma we handle, skip
                continue

            # Variables to track block boundaries
            let_start = -1
            let_end = -1
            in_start = -1
            in_end = -1

            if has_for_clause:
                # This pragma has 'for' clause - expect a for loop after the pragma clauses
                for_loop_spec, loop_body_start, loop_body_end = self._parse_for_loop(source, search_start)

                if loop_body_start != -1 and loop_body_end != -1:
                    # The Let and In blocks are inside the for loop body
                    loop_body = source[loop_body_start + 1:loop_body_end - 1]

                    # Find Let block inside loop body
                    let_content, let_rel_start, let_rel_end = self._extract_block_content(loop_body, 'Let')
                    if let_rel_start != -1:
                        let_start = loop_body_start + 1 + let_rel_start
                        let_end = loop_body_start + 1 + let_rel_end

                    # Find In block inside loop body (search after Let block)
                    in_search_start = let_rel_end if let_rel_end != -1 else 0
                    in_content, in_rel_start, in_rel_end = self._extract_block_content(loop_body, 'In', in_search_start)
                    if in_rel_start != -1:
                        in_start = loop_body_start + 1 + in_rel_start
                        in_end = loop_body_start + 1 + in_rel_end

                    # The pragma ends at the end of the for loop
                    end_pos = loop_body_end
                else:
                    # No valid for loop found, skip this pragma
                    print(f"Warning: #pragma with 'for' clause at line {source[:start_pos].count(chr(10)) + 1} has no valid for loop")
                    continue

            else:
                # No 'for' clause - Let and In blocks come directly after the pragma line
                # The Let and In blocks come directly after the pragma

                # Find Let block
                let_content, let_start, let_end = self._extract_block_content(source, 'Let', search_start)

                # Find In block (search after Let block if found)
                in_search_start = let_end if let_end != -1 else search_start
                in_content, in_start, in_end = self._extract_block_content(source, 'In', in_search_start)

                if in_end == -1:
                    print(f"Warning: #pragma at line {source[:start_pos].count(chr(10)) + 1} has no valid In block")
                    continue

                # The pragma ends at the end of the In block
                end_pos = in_end

            # Validate we found at least an In block
            if in_end == -1:
                continue

            idiom_text = source[start_pos:end_pos]
            blocks.append((start_pos, end_pos, idiom_text))

        return blocks

    # -------------------------------------------------------------------------
    # Main Parsing Methods
    # -------------------------------------------------------------------------

    def _parse_idiom_block(self, idiom_text: str) -> IdiomConstruct:
        """
        Parse a single pragma block into a IdiomConstruct structure.

        This method extracts all components from the pragma text:
        - Determines if pragma has a 'for' clause (can appear anywhere in clauses)
        - Parses all reduction clauses (multiple allowed)
        - Parses onComplete clause
        - Parses the for loop header if present
        - Extracts Let block declarations with parsed array accesses
        - Extracts In block content and store operations

        Args:
            idiom_text: The complete pragma text from '#pragma' to end of In block

        Returns:
            IdiomConstruct object with all parsed data
        """
        idiom = IdiomConstruct(original_text=idiom_text)

        # Strip comments from idiom_text for parsing
        # This ensures inline comments like "// reduction(+, sum)" are ignored
        idiom_text_clean = self._strip_comments(idiom_text)

        # Extract the pragma clause line (first line or up to 'for(' loop start)
        first_newline = idiom_text_clean.find('\n')
        idiom_line = idiom_text_clean[:first_newline] if first_newline != -1 else idiom_text_clean

        # Determine if 'for' clause is present (not followed by '(' which would be the loop)
        # The 'for' keyword in clauses is standalone, the actual for loop is 'for('
        has_for_clause = bool(re.search(r'\bfor\b(?!\s*\()', idiom_line))
        idiom.has_loop = has_for_clause

        # Parse all reduction clauses (multiple allowed) - use cleaned text
        idiom.reductions = self._parse_reductions(idiom_text_clean)

        # Parse onComplete clause (present in both types) - use cleaned text
        idiom.on_complete = self._parse_oncomplete(idiom_text_clean)

        # Parse numLanes (only 1 allowed) - use cleaned text
        idiom.num_lanes = self._parse_num_lanes(idiom_text_clean)

        # Parse maxRequestsInFlight (only 1 allowed) - use cleaned text
        idiom.max_requests_in_flight = self._parse_max_requests_in_flight(idiom_text_clean)

        # Parse scratchpadOffset (only 1 allowed) - use cleaned text
        idiom.scratchpad_offset = self._parse_scratchpad_offset(idiom_text_clean)

        # Get loop variable name for index classification (None if no loop)
        loop_var = None

        if has_for_clause:
            # Parse the for loop header - use cleaned text
            for_loop_spec, loop_body_start, loop_body_end = self._parse_for_loop(idiom_text_clean, 0)
            idiom.for_loop = for_loop_spec

            # Extract loop variable name for index classification
            if for_loop_spec:
                loop_var = for_loop_spec.var_name

            if loop_body_start != -1 and loop_body_end != -1:
                # Extract Let and In from inside the loop body - use cleaned text
                loop_body = idiom_text_clean[loop_body_start + 1:loop_body_end - 1]

                let_content, _, let_rel_end = self._extract_block_content(loop_body, 'Let')
                if let_content:
                    idiom.let_block_raw = let_content.strip()
                    # Pass loop_var to correctly classify array indices
                    idiom.let_declarations = self._parse_let_declarations(let_content, loop_var)

                in_search = let_rel_end if let_rel_end != -1 else 0
                in_content, _, _ = self._extract_block_content(loop_body, 'In', in_search)
                if in_content:
                    idiom.in_body = in_content.strip()
                    # Parse store operations from the In block
                    let_var_names = idiom.get_let_var_names()
                    idiom.store_operations = self._parse_store_operations(
                        in_content, let_var_names, loop_var
                    )
                    # Parse In-block expressions for unrolling
                    reduction_vars = [r.variable for r in idiom.reductions]
                    idiom.parsed_in_block = self._parse_in_block(
                        in_content, idiom.let_declarations, reduction_vars, loop_var
                    )
        else:
            # No loop - extract Let and In directly - use cleaned text
            let_content, _, let_end = self._extract_block_content(idiom_text_clean, 'Let')
            if let_content:
                idiom.let_block_raw = let_content.strip()
                # No loop variable for non-loop idioms
                idiom.let_declarations = self._parse_let_declarations(let_content, loop_var)

            in_search = let_end if let_end != -1 else 0
            in_content, _, _ = self._extract_block_content(idiom_text_clean, 'In', in_search)
            if in_content:
                idiom.in_body = in_content.strip()
                # Parse store operations from the In block
                let_var_names = idiom.get_let_var_names()
                idiom.store_operations = self._parse_store_operations(
                    in_content, let_var_names, loop_var
                )
                # Parse In-block expressions for unrolling
                reduction_vars = [r.variable for r in idiom.reductions]
                idiom.parsed_in_block = self._parse_in_block(
                    in_content, idiom.let_declarations, reduction_vars, loop_var
                )

        return idiom

    def process(self, source: str) -> Tuple[str, List[IdiomConstruct]]:
        """
        Process UDweave source code to extract pragma blocks.

        This is the main entry point for the preprocessor. It:
        1. Finds all #pragma for/onComplete blocks in the source
        2. Parses each block into a IdiomConstruct structure
        3. Removes the pragma blocks from the source
        4. Returns the cleaned source and list of parsed idioms

        The cleaned source has pragma blocks replaced with placeholder comments
        that preserve line numbers for error reporting.

        Args:
            source: The UDweave source code to process

        Returns:
            Tuple of:
                - clean_source: Source code with pragma blocks replaced by placeholders
                - idioms: List of IdiomConstruct objects for each pragma found

        Example:
            preprocessor = IdiomParser()
            clean_source, idioms = preprocessor.process(source_code)

            for idiom in idioms:
                if idiom.has_loop:
                    print(f"Loop: {idiom.for_loop}")
                print(f"Let vars: {idiom.get_let_var_names()}")
                print(f"In body: {idiom.in_body}")
        """
        idioms = []
        blocks = self.find_idiom_blocks(source)

        # Process blocks in reverse order to maintain correct positions
        # when modifying the source string (later blocks have higher indices)
        clean_source = source
        for start, end, idiom_text in reversed(blocks):
            # Calculate line numbers for error reporting
            start_line = source[:start].count('\n') + 1
            end_line = source[:end].count('\n') + 1

            # Parse the pragma block into structured data
            parsed = self._parse_idiom_block(idiom_text)
            parsed.start_line = start_line
            parsed.end_line = end_line

            # Extract type context from surrounding source code
            parsed.type_context = self._extract_type_context(source, start_line)

            # Apply type information to store operations
            self._apply_type_context_to_stores(parsed)

            idioms.insert(0, parsed)  # Insert at beginning to maintain order

            # Replace pragma block with a placeholder comment
            # Preserve newlines to maintain line numbers for error reporting in main parser
            newlines = idiom_text.count('\n')
            placeholder = f"/* IDIOM_CONSTRUCT_{len(idioms)-1} */" + '\n' * newlines
            clean_source = clean_source[:start] + placeholder + clean_source[end:]

        return clean_source, idioms

    def get_placeholder_indices(self, source: str) -> dict:
        """
        Find placeholder comments in processed source and return their positions.

        This is useful for the code generator to know where to insert
        generated code for each pragma.

        Args:
            source: Processed source code (output from process())

        Returns:
            Dictionary mapping pragma index to line number
        """
        indices = {}
        for match in re.finditer(r'/\* IDIOM_CONSTRUCT_(\d+) \*/', source):
            idx = int(match.group(1))
            line = source[:match.start()].count('\n') + 1
            indices[idx] = line
        return indices

    # print out all relevant info about the pragma for debugging
    def toString(self, idioms, clean_source) -> str:
        """
        Generate a detailed string representation of parsed idioms.

        Includes all parsed information:
        - Loop specification (if present)
        - Reduction and onComplete clauses
        - Let declarations with parsed array access details
        - Store operations from In block
        - Dependency analysis

        Args:
            idioms: List of IdiomConstruct objects
            clean_source: The source code with idioms replaced by placeholders

        Returns:
            Formatted string with all pragma details
        """
        res = f"\nFound {len(idioms)} idiom(s)"

        for i, idiom in enumerate(idioms):
            res += f"\n{'='*60}\n"
            res += f"Idiom {i}\n"
            res += f"{'='*60}\n"

            # Basic idiom info
            res += f"\n[Loop Information]\n"
            res += f"\tHas loop: {idiom.has_loop}\n"
            if idiom.for_loop:
                loop = idiom.for_loop
                res += f"\tFor loop: {loop}\n"
                res += f"\t\tLoop variable: {loop.var_name} ({' '.join(loop.var_qualifiers)} {loop.var_type})\n" if loop.var_qualifiers else f"\t\tLoop variable: {loop.var_name} ({loop.var_type})\n"

                # Raw values
                res += f"\t\t[Raw values]\n"
                res += f"\t\t\tInit: {loop.raw_init}\n"
                res += f"\t\t\tCondition: {loop.raw_condition}\n"
                res += f"\t\t\tIncrement: {loop.raw_increment}\n"

                # Parsed values
                res += f"\t\t[Parsed values]\n"
                if loop.start:
                    if loop.start.is_constant:
                        res += f"\t\t\tStart: {loop.start.constant_value} (constant)\n"
                    elif loop.start.variable_name:
                        res += f"\t\t\tStart: {loop.start.variable_name} (variable)\n"
                    else:
                        res += f"\t\t\tStart: {loop.start.raw_expr} (expression)\n"

                if loop.end:
                    if loop.end.is_constant:
                        res += f"\t\t\tEnd: {loop.end.constant_value} (constant)\n"
                    elif loop.end.variable_name:
                        res += f"\t\t\tEnd: {loop.end.variable_name} (variable)\n"
                    else:
                        res += f"\t\t\tEnd: {loop.end.raw_expr} (expression)\n"

                res += f"\t\t\tComparison: {loop.comparison_op}\n"

                if loop.stride:
                    if loop.stride.is_constant:
                        res += f"\t\t\tStride: {loop.stride.constant_value} (constant)\n"
                    elif loop.stride.variable_name:
                        res += f"\t\t\tStride: {loop.stride.variable_name} (variable)\n"
                    else:
                        res += f"\t\t\tStride: {loop.stride.raw_expr} (expression)\n"
                    direction_str = "increasing" if loop.stride.direction > 0 else "decreasing" if loop.stride.direction < 0 else "unknown"
                    res += f"\t\t\tDirection: {direction_str}\n"

            # Clauses
            res += f"\n[Idiom Clauses]\n"
            res += f"\tReductions ({len(idiom.reductions)}):\n"
            if idiom.reductions:
                for red in idiom.reductions:
                    res += f"\t\t{red}\n"
            else:
                res += f"\t\tNone\n"
            res += f"\tOnComplete: {idiom.on_complete}\n"

            # Let declarations with parsed array access
            res += f"\n[Let Declarations] ({len(idiom.let_declarations)} total)\n"
            for decl in idiom.let_declarations:
                res += f"\t{decl.var_name}:\n"
                res += f"\t\tType: {' '.join(decl.qualifiers)} {decl.var_type}\n" if decl.qualifiers else f"\t\tType: {decl.var_type}\n"
                res += f"\t\tSource expr: {decl.source_expr}\n"
                if decl.parsed_source:
                    ps = decl.parsed_source
                    res += f"\t\tParsed array access:\n"
                    res += f"\t\t\tArray name: {ps.array_name}\n"
                    res += f"\t\t\tIndex: {ps.index}\n"
                    res += f"\t\t\tIndex type: {ps.index.index_type.name}\n"
                    if ps.index.index_type == IndexType.CONSTANT:
                        res += f"\t\t\tConstant value: {ps.index.constant_value}\n"
                    elif ps.index.index_type in (IndexType.LOOP_VAR, IndexType.VARIABLE):
                        res += f"\t\t\tVariable: {ps.index.base_variable}\n"
                    if ps.index.involves_loop_var:
                        res += f"\t\t\tInvolves loop var: Yes\n"
                else:
                    res += f"\t\tParsed array access: None (not an array access)\n"

            # In block content
            res += f"\n[In Block]\n"
            res += f"\tRaw content: {idiom.in_body}\n"
            if idiom.parsed_in_block:
                res += f"\t[Parsed Statements] ({len(idiom.parsed_in_block.statements)} total)\n"
                for j, stmt in enumerate(idiom.parsed_in_block.statements):
                    res += f"\t\tStatement {j}: {stmt.target_var} {stmt.assignment_type.value} ...\n"
                    if stmt.value_expr:
                        res += f"\t\t\tExpression: {stmt.value_expr.generate_with_substitutions({})}\n"

            # Store operations
            res += f"\n[Store Operations] ({len(idiom.store_operations)} total)\n"
            if idiom.store_operations:
                for store in idiom.store_operations:
                    res += f"\tStore to {store.array_name}:\n"
                    if store.array_type:
                        res += f"\t\tArray type: {store.array_type.full_type_str()} (from {store.array_type.source})\n"
                    else:
                        res += f"\t\tArray type: unknown\n"
                    res += f"\t\tIndex: {store.index}\n"
                    res += f"\t\tIndex type: {store.index.index_type.name}\n"
                    res += f"\t\tValue expr: {store.value_expr}\n"
                    res += f"\t\tSource Let vars: {store.source_let_vars if store.source_let_vars else 'none'}\n"
                    res += f"\t\tRaw statement: {store.raw_statement}\n"
            else:
                res += f"\tNo store operations found\n"

            # Type context
            if idiom.type_context:
                res += f"\n[Type Context] ({len(idiom.type_context)} variables)\n"
                for var_name, type_info in idiom.type_context.items():
                    res += f"\t{var_name}: {type_info.full_type_str()} (from {type_info.source})\n"

            # Line info
            res += f"\n[Source Location]\n"
            res += f"\tLines: {idiom.start_line}-{idiom.end_line}\n"

            # Dependencies analysis
            res += f"\n[Dependencies Analysis]\n"
            deps = idiom.get_dependencies()
            res += f"\tLet vars: {deps['let_vars']}\n"
            if deps['let_var_types']:
                for var, typ in deps['let_var_types'].items():
                    res += f"\t\t{var}: {typ}\n"
            res += f"\tLoop var: {deps['loop_var']}"
            if deps['loop_var_type']:
                res += f" ({deps['loop_var_type']})"
            res += f"\n"
            res += f"\tReduction vars: {deps['reduction_vars']}\n"
            if deps['reduction_var_types']:
                for var, type_info in deps['reduction_var_types'].items():
                    res += f"\t\t{var}: {type_info.full_type_str()}\n"
            res += f"\t[In Block Variables]\n"
            res += f"\t\tAll vars in In: {deps['in_all_vars']}\n"
            res += f"\t\tLet vars used: {deps['in_uses_let_vars']}\n"
            res += f"\t\tUses loop var: {deps['in_uses_loop_var']}\n"
            res += f"\t\tOther vars: {deps['in_other_vars']}\n"
            if deps['in_other_var_types']:
                res += f"\t\tOther var types:\n"
                for var, type_info in deps['in_other_var_types'].items():
                    res += f"\t\t\t{var}: {type_info.full_type_str()}\n"

        res += f"Max requests in flight: {idiom.max_requests_in_flight}\n"
        res += f"Num lanes: {idiom.num_lanes}\n"
        res += f"Scratchpad offset: {idiom.scratchpad_offset}\n"

        res += f"\n{'='*60}\n"
        res += f"Cleaned Source (first 300 chars)\n"
        res += f"{'='*60}\n"
        # res += clean_source[:300]


        # add comments to the result so that it can be directly used in the UDW compiler.
        res_lines = res.split('\n')
        commented_lines = [f"# {line}" for line in res_lines]
        res = '\n'.join(commented_lines)
        res += "\n"+clean_source
        return res


# =============================================================================
# Convenience Functions
# =============================================================================

def preprocess_idioms(source: str) -> Tuple[str, List[IdiomConstruct]]:
    """
    Convenience function to preprocess pragma blocks from source code.

    Args:
        source: UDweave source code

    Returns:
        Tuple of (clean_source, list_of_idioms)
    """
    preprocessor = IdiomParser()
    return preprocessor.process(source)


# =============================================================================
# Test Code
# =============================================================================

if __name__ == '__main__':
    # Test with the three idiom patterns

    # Idiom 1: Simple Let/In without loop
    idiom1 = '''
thread T {
    event e(long* myArray) {
        long localvar = 0;
        #pragma onComplete(eventOnComplete, localvar)
        Let {
            long a = myArray[16];
            long b = myArray[6];
        }
        In {
            localvar = a+b;
        }
    }

    event eventOnComplete(long localvar) {
        print("%d", localvar);
    }
}
'''

    # Idiom 2: For loop with reduction
    idiom2 = '''
#define LIMIT 1048572

thread T {
    event e(long* myArrayA, long* myArrayB) {
        long sum = 0;
        #pragma for reduction(+, sum) onComplete(eventOnComplete, sum)
        for(unsigned long i=0; i<LIMIT; i++) {
            Let {
                long a = myArrayA[i];
                long b = myArrayB[i];
            }
            In {
                sum = sum + a * b;
            }
        }
    }

    event eventOnComplete(long sum) {
        print("%d", sum);
    }
}
'''

    # Idiom 3: For loop without reduction
    idiom3 = '''
#define LIMIT 1048572

thread T {
    event e(long* myArrayA, long* myArrayB) {
        long sum = 0;
        #pragma for onComplete(eventOnComplete)
        for(unsigned long i=0; i<LIMIT; i++) {
            Let {
                long a = myArrayA[i];
            }
            In {
                myArrayB[i] = a;
            }
        }
    }

    event eventOnComplete() {
        print("Complete");
    }
}
'''

    print("=" * 70)
    print("Testing IdiomParser with Idiom Examples")
    print("=" * 70)

    preprocessor = IdiomParser()

    for name, test_source in [("Idiom 1 (no loop)", idiom1),
                               ("Idiom 2 (loop + reduction)", idiom2),
                               ("Idiom 3 (loop, no reduction)", idiom3)]:
        print(f"\n{'='*70}")
        print(f"Testing: {name}")
        print("=" * 70)

        clean_source, idioms = preprocessor.process(test_source)

        print(f"\nFound {len(idioms)} idiom(s)")

        for i, idiom in enumerate(idioms):
            print(f"\n--- Pragma {i} ---")
            print(f"  Has loop: {idiom.has_loop}")
            if idiom.for_loop:
                print(f"  For loop: {idiom.for_loop}")
            print(f"  Reduction: {idiom.reductions}")
            print(f"  OnComplete: {idiom.on_complete}")
            print(f"  Let declarations ({len(idiom.let_declarations)}):")
            for decl in idiom.let_declarations:
                print(f"    - {decl}")
            print(f"  In body: {idiom.in_body}")
            print(f"  Lines: {idiom.start_line}-{idiom.end_line}")

            print("\n  Dependencies analysis:")
            deps = idiom.get_dependencies()
            print(f"    Let vars: {deps['let_vars']}")
            print(f"    Loop var: {deps['loop_var']}")
            print(f"    Used in In: {deps['in_uses']}")
            print(f"    In uses loop var: {deps['in_uses_loop_var']}")
            print(f"    Reduction var: {deps['reduction_var']}")

        print(f"\n--- Cleaned Source (first 300 chars) ---")
        print(clean_source[:300])
