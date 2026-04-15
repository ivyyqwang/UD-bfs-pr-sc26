from abc import ABC, abstractmethod
from typing import Dict, List, Optional

from Weave.debug import errorMsg
from frontend.idiom_parser import (
    IdiomConstruct, OnCompleteSpec, ForLoopSpec, LetDeclaration,
    ParsedInBlock, InBlockStatement, InBlockExpr, ExprType, BinaryOp, StoreOperation, VariableTypeInfo
)
import random
import string
from enum import Enum, auto
import Weave.debug as debug


class ReductionStrategy(Enum):
    """Strategy for handling reduction operations during unrolling."""
    SEQUENTIAL = auto()       # Each iteration updates target: sum = sum + expr0; sum = sum + expr1; ...
    SINGLE_EXPRESSION = auto()  # Combine all in one: sum = sum + expr0 + expr1 + ... + expr7;
    ACCUMULATOR = auto()      # Use local accumulators: acc = expr0 + expr1...; sum = sum + acc;


class IdiomLoopDefinition:
    class LoopDirection(Enum):
        FORWARD = 1
        BACKWARD = 2
        UNKNOWN = 3

    def __init__(self):
        self.loopComparison = ""
        self.stride = 0
        self.direction = IdiomLoopDefinition.LoopDirection.UNKNOWN
        self.staticBounds = True

    def __str__(self):
        return (f"IdiomLoopDefinition(loopComparison={self.loopComparison}, "
                f"stride={self.stride}, direction={self.direction}, staticBounds={self.staticBounds})")



class IdiomDefinition:
    def __init__(self):
        self.loop: Optional[IdiomLoopDefinition] = None
        self.let_declarations = {'min': 0, 'max': 0}
        self.stores = 0
        self.needsScratchpadOffset = False

    def _checkLoopParams(self, idiom: IdiomConstruct) -> bool:
        idiomLoop: ForLoopSpec = idiom.for_loop
        if idiomLoop and self.loop:
            # direction
            debug.debugMsg(3, f"\tChecking loop direction: idiomLoop.stride.direction: "
                              f"{idiomLoop.stride.direction}, self.loop.direction: {self.loop.direction}")
            if (idiomLoop.stride.direction < 0 and self.loop.direction == IdiomLoopDefinition.LoopDirection.FORWARD or
                idiomLoop.stride.direction > 0 and self.loop.direction == IdiomLoopDefinition.LoopDirection.BACKWARD):
                return False

            # stride
            debug.debugMsg(3, f"\tChecking loop stride: idiomLoop.stride.constant_value: "
                              f"{idiomLoop.stride.constant_value}, self.loop.stride: {self.loop.stride}")
            if idiomLoop.stride.constant_value != self.loop.stride:
                return False

            # checking for static loop bounds
            debug.debugMsg(3, f"\tChecking boundaries: "
                              f"idiomLoop.end.variable_name: {idiomLoop.end.variable_name}, "
                              f"idiomLoop.start.variable_name: {idiomLoop.start.variable_name}, "
                              f"idiomLoop.end.constant_value: {idiomLoop.end.constant_value}, "
                              f"idiomLoop.start.constant_value: {idiomLoop.start.constant_value}, "
                              f"self.loop.staticBounds: {self.loop.staticBounds}")
            if self.loop.staticBounds:
                if idiomLoop.end.variable_name is not None or idiomLoop.start.variable_name is not None:
                    return False
            else:
                if idiomLoop.end.constant_value is not None and idiomLoop.start.constant_value is not None:
                    return False
            return True

        elif not idiomLoop and not self.loop:
            return True

        return False

    def checkIdiom(self, idiom: IdiomConstruct) -> bool:
        # check, if we need to have scratchpad enabled
        if self.needsScratchpadOffset and idiom.scratchpad_offset is None:
            debug.debugMsg(3, f"Idiom does not match: needsScratchpadOffset: {self.needsScratchpadOffset}, idiom.scratchpad_offset: {idiom.scratchpad_offset}")
            return False

        checkLoop = self._checkLoopParams(idiom)
        numDecl = len(idiom.let_declarations)
        numStores = len(idiom.store_operations)
        debug.debugMsg(3, f"Checking Idiom: loop check: {checkLoop}, let decl check: {self.let_declarations['min']} <= {numDecl} <= {self.let_declarations['max']}, store check: {self.stores} == {numStores}")
        return (
            checkLoop and
            self.let_declarations['min'] <= numDecl <= self.let_declarations['max'] and
            self.stores == numStores
        )

    def __str__(self):
        return (f"IdiomDefinition(loop={self.loop}, "
                f"let_declarations={self.let_declarations}, stores={self.stores})")



class WeaveIdiom(ABC):

    def __init__(self):
        self.thread_name = ""
        self.idiom = None
        self.startEventParams = ""
        self.startEventVars = ""
        self.threadParamsDecl = ""
        self.threadParamsInit = ""


    @classmethod
    @abstractmethod
    def getName(cls) -> str:
        pass

    @abstractmethod
    def generate(self) -> str:
        pass

    @abstractmethod
    def getDefinition(self) -> IdiomDefinition:
        pass


    def getStartEventParams(self):

        seenVars = set()
        params_data = []  # List of tuples: (startEventParams, startEventVars, threadParamsDecl, threadParamsInit)

        def populate(varName: str):
            var: VariableTypeInfo = self.idiom.type_context[varName]
            if not var:
                errorMsg(f"Could not determine type of variable {varName}. Is the array declared locally?")

            if var.var_name in seenVars:
                return

            ptrText = "*" if var.is_pointer else ""
            seenVars.add(var.var_name)
            params_data.append([
                f"{var.base_type}{ptrText} _{var.var_name}",
                var.var_name,
                f"{var.base_type}{ptrText} {var.var_name};",
                f"{var.var_name} = _{var.var_name};"])



        # Handle the let declaration
        for decl in self.idiom.let_declarations:
            if decl.parsed_source:
                populate(decl.parsed_source.array_name)

        # handle declarations in the In-Block that come from outside of the context
        # filter out variables of the Let Block
        inBlockVars = self.idiom.get_dependencies()['in_other_vars']
        for decl in inBlockVars:
            if decl in self.idiom.type_context:
                populate(decl)

        if self.idiom.for_loop:
            if self.idiom.for_loop.start.variable_name:
                populate(self.idiom.for_loop.start.variable_name)
            if self.idiom.for_loop.end.variable_name:
                populate(self.idiom.for_loop.end.variable_name)

        # Handle the store operation
        for decl in self.idiom.store_operations:
            populate(decl.array_name)

        self.startEventParams = ', '.join([p[0] for p in params_data])
        self.startEventVars = ', '.join([p[1] for p in params_data])
        self.threadParamsDecl = '\n'.join([p[2] for p in params_data])
        self.threadParamsInit = '\n'.join([p[3] for p in params_data])


    def insertion(self):
        varID = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        contWord = self.idiom.on_complete.event_name

        eventVars = self.startEventVars.split(',')

        if len(eventVars) > 3 and self.idiom.scratchpad_offset is None:
            errorMsg(
                "Number of input parameters for the idiom in "
                f"lines {self.idiom.start_line}-{self.idiom.end_line} exceeds 3!\n"
                f"Configure a scratchpad offset to pass more than 3 parameters.\nParameters: {eventVars}\n"
            )

        if len(eventVars) > 8:
            errorMsg(
                "Number of input parameters for the idiom in "
                f"lines {self.idiom.start_line}-{self.idiom.end_line} exceeds 8!\nParameters: {eventVars}\n"
            )

        res = f"""
            unsigned long evw_{varID} = evw_new(NETID, {self.thread_name}::start);
            unsigned long cont_{varID} = evw_update_event(CEVNT, {contWord});
        """

        if len(eventVars) > 3:
            res += f"unsigned long* local sp_offset_{varID} = LMBASE + {self.idiom.scratchpad_offset};\n"
            for i, param in enumerate(eventVars):
                res += f"sp_offset_{varID}[{i}] = {param};\n"

            res += f"send_event(evw_{varID}, sp_offset_{varID}, {len(eventVars)}, cont_{varID});\n"
        else:
            res += f"send_event(evw_{varID}, {self.startEventVars}, cont_{varID});\n"
        return res

    def setIdiom(self, idiom: IdiomConstruct):
        self.idiom = idiom

    @classmethod
    def allIdioms(cls) -> list:
        """Returns all available idioms
        Returns:
            list: list of idiom class references
        """
        return list(cls.__getAllSubclasses())

    @classmethod
    def __getAllSubclasses(cls):
        result = set()
        for s in cls.__subclasses__():
            result.add(s)
            result.update(s.__getAllSubclasses())
        return result


    @classmethod
    def checkIdiom(cls, idiom: IdiomConstruct):
        supported_idioms = cls.allIdioms()
        for idiom_cls in supported_idioms:
            iDef: IdiomDefinition = idiom_cls().getDefinition()
            debug.debugMsg(2, f"Checking Idiom: {iDef}")
            if iDef and iDef.checkIdiom(idiom):
                return idiom_cls

        return None


    def __eq__(self, other) -> bool:
        if not isinstance(other, WeaveIdiom):
            return False
        return self.getName() == other.getName()

    # =========================================================================
    # In-Block Unrolling Methods
    # =========================================================================

    def _unrollInBlock(self,
                       unroll_factor: int,
                       substitutions: Dict[str, str],
                       indent: str = "",
                       reduction_strategy: ReductionStrategy = ReductionStrategy.SEQUENTIAL,
                       generate_declarations: bool = False,
                       append_index_to: Optional[set] = None) -> str:
        """
        Generate unrolled In-block code with variable substitutions and reduction awareness.

        This method uses the parsed In-block expression tree to generate unrolled code
        where specified variables are substituted according to the given patterns.

        Args:
            unroll_factor: Number of iterations to unroll (e.g., 8 for 64-byte cache line
                          with 8-byte elements)
            substitutions: Mapping of variable names to replacement patterns.
                          Use {i} as placeholder for unroll index (0 to unroll_factor-1).
                          Example: {'a': 'var{i}', 'b': '_var{i}'}
                          Variables not in this dict and not in append_index_to remain
                          unchanged in all copies.
            indent: String to prepend to each generated line for formatting
            reduction_strategy: How to handle reduction variables:
                - SEQUENTIAL: Generate separate statements (default, simple)
                - SINGLE_EXPRESSION: Combine all iterations into one expression
                - ACCUMULATOR: Use a local accumulator variable
            generate_declarations: If True, generate declarations for temporary variables
                                  used in ACCUMULATOR strategy
            append_index_to: Set of variable names that should have the unroll index
                            appended, even if not in substitutions. For these variables,
                            'a' becomes 'a0', 'a1', etc.
                            Example: {'a', 'b'} with substitutions={'b': '_b{i}'}
                            Results in: a -> a0, a1, ...; b -> _b0, _b1, ...

        Returns:
            String containing the unrolled In-block code

        Example:
            For In-block: sum = sum + a * b;
            With substitutions: {'b': '_b{i}'}, append_index_to: {'a'}
            And unroll_factor: 8

            SEQUENTIAL generates:
                sum = sum + a0 * _b0;
                sum = sum + a1 * _b1;
                ...
                sum = sum + a7 * _b7;

            With substitutions: {'a': 'var{i}', 'b': '_var{i}'}
            And unroll_factor: 8

            SEQUENTIAL generates:
                sum = sum + var0 * _var0;
                sum = sum + var1 * _var1;
                ...
                sum = sum + var7 * _var7;

            SINGLE_EXPRESSION generates:
                sum = sum + (var0 * _var0) + (var1 * _var1) + ... + (var7 * _var7);

            ACCUMULATOR generates:
                long _acc_sum = (var0 * _var0) + (var1 * _var1) + ... + (var7 * _var7);
                sum = sum + _acc_sum;

        Raises:
            ValueError: If idiom has no parsed_in_block or unroll_factor < 1
        """
        if not self.idiom or not self.idiom.parsed_in_block:
            raise ValueError("Idiom must have a parsed In-block for unrolling")
        if unroll_factor < 1:
            raise ValueError("unroll_factor must be >= 1")

        parsed_in_block: ParsedInBlock = self.idiom.parsed_in_block
        reduction_map = self._getReductionMap()
        append_index_to = append_index_to or set()

        lines = []

        for stmt in parsed_in_block.statements:
            target_var = stmt.target_var
            reduction_op = reduction_map.get(target_var)

            if reduction_op and reduction_strategy != ReductionStrategy.SEQUENTIAL:
                # Handle reduction with optimized strategy
                code = self._generateReductionUnroll(
                    stmt, unroll_factor, substitutions, reduction_op,
                    reduction_strategy, indent, generate_declarations,
                    append_index_to
                )
                lines.append(code)
            else:
                # Standard sequential unrolling
                for i in range(unroll_factor):
                    line = self._generateSingleUnroll(stmt, i, substitutions, append_index_to)
                    lines.append(f"{indent}{line}")

        return "\n".join(lines)

    def _getReductionMap(self) -> Dict[str, str]:
        """
        Build a mapping from reduction variable names to their operators.

        Returns:
            Dict mapping variable name to operator (e.g., {'sum': '+', 'prod': '*'})
        """
        if not self.idiom or not self.idiom.reductions:
            return {}
        return {r.variable: r.operator for r in self.idiom.reductions}

    def _generateSingleUnroll(self,
                              stmt: InBlockStatement,
                              unroll_index: int,
                              substitutions: Dict[str, str],
                              append_index_to: Optional[set] = None) -> str:
        """
        Generate code for a single iteration of an unrolled statement.

        Args:
            stmt: The statement to unroll
            unroll_index: The iteration index (0 to unroll_factor-1)
            substitutions: Variable substitution patterns with {i} placeholder
            append_index_to: Set of variable names that should have index appended
                            even if not in substitutions

        Returns:
            Single statement string with substitutions applied
        """
        append_index_to = append_index_to or set()

        # Build substitutions for this specific index
        resolved_subs = {
            var_name: pattern.format(i=unroll_index)
            for var_name, pattern in substitutions.items()
        }

        # For variables in append_index_to but NOT in substitutions,
        # add them with simple index appending: var -> var0, var1, etc.
        for var_name in append_index_to:
            if var_name not in resolved_subs:
                resolved_subs[var_name] = f"{var_name}{unroll_index}"

        # Generate the RHS expression with substitutions
        if stmt.value_expr:
            rhs = stmt.value_expr.generate_with_substitutions(resolved_subs)
        else:
            rhs = ""

        target = stmt.target_var
        op = stmt.assignment_type.value
        return f"{target} {op} {rhs};"

    def _generateReductionUnroll(self,
                                 stmt: InBlockStatement,
                                 unroll_factor: int,
                                 substitutions: Dict[str, str],
                                 reduction_op: str,
                                 strategy: ReductionStrategy,
                                 indent: str,
                                 generate_declarations: bool,
                                 append_index_to: Optional[set] = None) -> str:
        """
        Generate optimized reduction code for unrolling.

        For a statement like 'sum = sum + a * b' with reduction '+':
        - Extracts the value expression (a * b)
        - Generates unrolled versions of just the value part
        - Combines them according to the strategy

        Args:
            stmt: The reduction statement
            unroll_factor: Number of iterations
            substitutions: Variable substitution patterns
            reduction_op: The reduction operator ('+', '*', etc.)
            strategy: SINGLE_EXPRESSION or ACCUMULATOR
            indent: Line indentation
            generate_declarations: Whether to generate temp variable declarations
            append_index_to: Set of variable names that should have index appended
                            even if not in substitutions

        Returns:
            Generated code string
        """
        append_index_to = append_index_to or set()
        target_var = stmt.target_var

        # Extract the "value" part of the reduction (e.g., 'a * b' from 'sum = sum + a * b')
        value_parts = self._extractReductionValues(stmt.value_expr, target_var, reduction_op)

        if not value_parts:
            # Fallback to sequential if we can't extract reduction structure
            lines = []
            for i in range(unroll_factor):
                lines.append(f"{indent}{self._generateSingleUnroll(stmt, i, substitutions, append_index_to)}")
            return "\n".join(lines)

        # Generate unrolled value expressions
        unrolled_values = []
        for i in range(unroll_factor):
            resolved_subs = {
                var_name: pattern.format(i=i)
                for var_name, pattern in substitutions.items()
            }
            # Add variables from append_index_to that aren't in substitutions
            for var_name in append_index_to:
                if var_name not in resolved_subs:
                    resolved_subs[var_name] = f"{var_name}{i}"

            for value_expr in value_parts:
                unrolled_values.append(value_expr.generate_with_substitutions(resolved_subs))

        if strategy == ReductionStrategy.SINGLE_EXPRESSION:
            # Combine all into one expression: sum = sum + (v0*w0) + (v1*w1) + ...
            combined = f" {reduction_op} ".join(unrolled_values)
            return f"{indent}{target_var} = {target_var} {reduction_op} {combined};"

        elif strategy == ReductionStrategy.ACCUMULATOR:
            # Use accumulator: _acc = (v0*w0) + (v1*w1) + ...; sum = sum + _acc;
            lines = []
            combined = f" {reduction_op} ".join(unrolled_values)
            acc_type = self._inferTypeForVar(target_var)

            if generate_declarations:
                lines.append(f"{indent}{acc_type} _acc_{target_var} = {combined};")
            else:
                lines.append(f"{indent}_acc_{target_var} = {combined};")

            lines.append(f"{indent}{target_var} = {target_var} {reduction_op} _acc_{target_var};")
            return "\n".join(lines)

        return ""

    def _extractReductionValues(self,
                                expr: InBlockExpr,
                                target_var: str,
                                reduction_op: str) -> List[InBlockExpr]:
        """
        Extract the value expressions from a reduction statement.

        For 'sum = sum + a * b', this extracts [a * b].
        For 'sum = sum + a + b', this extracts [a, b].

        The pattern we look for is: target = target OP expr1 OP expr2 OP ...

        Args:
            expr: The full RHS expression tree
            target_var: The reduction target variable name
            reduction_op: The reduction operator

        Returns:
            List of value expressions that should be unrolled
        """
        if not expr or expr.expr_type != ExprType.BINARY_OP:
            return []

        op_map = {'+': BinaryOp.ADD, '-': BinaryOp.SUB, '*': BinaryOp.MUL,
                  '&': BinaryOp.BITAND, '|': BinaryOp.BITOR, '^': BinaryOp.BITXOR}
        expected_op = op_map.get(reduction_op)

        if expr.binary_op != expected_op:
            return []

        # Check if left side is the target variable
        if (expr.left and expr.left.expr_type == ExprType.VARIABLE and
            expr.left.var_info and expr.left.var_info.name == target_var):
            # Pattern: target OP value_expr
            if expr.right:
                return [expr.right]

        # Check for chained operations: (target + a) + b => extract [a, b]
        # Recursively extract from left side if it's also a reduction pattern
        if expr.left and expr.left.expr_type == ExprType.BINARY_OP:
            left_values = self._extractReductionValues(expr.left, target_var, reduction_op)
            if left_values and expr.right:
                return left_values + [expr.right]

        return []

    def _inferTypeForVar(self, var_name: str) -> str:
        """
        Infer the type for a variable based on context.

        Args:
            var_name: The variable name

        Returns:
            Type string (defaults to 'long' if unknown)
        """
        # Check Let declarations
        if self.idiom and self.idiom.let_declarations:
            for decl in self.idiom.let_declarations:
                if decl.var_name == var_name:
                    qual = ' '.join(decl.qualifiers) + ' ' if decl.qualifiers else ''
                    return f"{qual}{decl.var_type}".strip()

        # Default to long for reduction variables
        return "long"

    def _getAccumulatorDeclarations(self) -> str:
        """
        Generate accumulator variable declarations for ACCUMULATOR strategy.

        Returns:
            Declaration statements for accumulator variables
        """
        if not self.idiom:
            return ""

        lines = []
        reduction_map = self._getReductionMap()

        for var_name in reduction_map.keys():
            var_type = self._inferTypeForVar(var_name)
            lines.append(f"{var_type} _acc_{var_name};")

        return "\n".join(lines)

    def _buildLetVarSubstitutions(self, first_pattern: str = "var{i}",
                                   second_pattern: str = "_var{i}") -> Dict[str, str]:
        """
        Build substitution patterns for Let variables based on declaration order.

        In the event-driven model:
        - First Let variable (e.g., 'a') comes from the first-returned DRAM read
        - Second Let variable (e.g., 'b') comes as event parameters

        Args:
            first_pattern: Pattern for the first Let variable (default: 'var{i}')
            second_pattern: Pattern for the second Let variable (default: '_var{i}')

        Returns:
            Dict mapping Let variable names to their substitution patterns
        """
        subs = {}
        if self.idiom and self.idiom.let_declarations:
            for idx, decl in enumerate(self.idiom.let_declarations):
                if idx == 0:
                    subs[decl.var_name] = first_pattern
                else:
                    subs[decl.var_name] = second_pattern
        return subs

    def _createUniqueThreadName(self):
        # create a unique thread module name
        uid = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        self.thread_name = f"Idiom_{self.getName()}_S{self.idiom.start_line}_E{self.idiom.end_line}_{uid}"

    def getReadCounter(self, init: int = -1, threshold: int = 2):
        readCounter = 0
        readCounterInit = ""
        readCounterDecl = ""

        for decl in self.idiom.let_declarations:
            if decl.parsed_source:
                readCounter += 1

        if readCounter >= threshold:
            readCounterDecl = "unsigned long readCounter;\n"
            if init >= 0:
                readCounterInit = f"                    readCounter = {init};"
            else:
                readCounterInit = f"                    readCounter = {readCounter};"

        return readCounter, readCounterDecl, readCounterInit

    def getTerminate(self, shouldYieldTerminate: bool) -> str:
        yieldT = "yield_terminate;\n" if shouldYieldTerminate else ""
        onComplete : OnCompleteSpec = self.idiom.on_complete
        if len(onComplete.arguments) > 3:
            errorMsg(
                "Number of onComplete arguments for idiom in "
                f"lines {self.idiom.start_line}-{self.idiom.end_line} exceeds 3!\n"
                "Cannot create the idiom."
            )
        if onComplete:
            if len(onComplete.arguments) > 0:
                args = ", ".join(onComplete.arguments)
                return f"send_event(CCONT, {args}, IGNRCONT);\n{yieldT}"
            else:
                return f"send_event(CCONT, 0 /* do not care */, IGNRCONT);\n{yieldT}"
        return yieldT

    def getLoopIterator(self):
        loop: ForLoopSpec = self.idiom.for_loop
        iteratorDecl = f"{' '.join(loop.var_qualifiers)} {loop.var_type} {loop.var_name};\n"
        iteratorInit = f"{loop.var_name} = {loop.start.constant_value};"
        return iteratorDecl, iteratorInit

    def getLoopBody(self, readCounterInit: str, unroll_factor: int) -> str:

        if unroll_factor == 0:
            return ""

        loop: ForLoopSpec = self.idiom.for_loop
        instructions = [readCounterInit.strip()]

        for i, letDecl in enumerate(self.idiom.let_declarations):
            if letDecl.parsed_source:
                arrayAccess = letDecl.parsed_source
                instructions.append(f"{' '.join(letDecl.qualifiers)} {letDecl.var_type}* {arrayAccess.array_name}Local"
                                    f" = {arrayAccess.array_name} + ({loop.var_name}*sizeof({letDecl.var_type}));")
                instructions.append(f"//print(\"%ld, RA: 0x%lx\", i, {arrayAccess.array_name}Local);")
                instructions.append(f"send_dram_read({arrayAccess.array_name}Local, {unroll_factor}, "
                                    f"read_return_{arrayAccess.array_name}{unroll_factor});")

        indent = "\n" + " " * 20
        res = indent.join(instructions)
        return res


class Array2Read(WeaveIdiom):
    """
    Idiom for reading at maximum 2 arrays with a constant index each. Example:
    ```
    event e() {
        long localvar = 0;
        #pragma onComplete(eventOnComplete, localvar)
        Let {
            long a = myArray[2];
            long b = myArray[23];
        }
        In {
            localvar = a+b;
        }

    	// do something with localvar
	    print(localvar); // prints 0
    }
    ```
    """

    @classmethod
    def getName(cls) -> str:
        return "Array2Read"

    @classmethod
    def getDefinition(cls) -> IdiomDefinition:
        idiomDef = IdiomDefinition()
        idiomDef.loop = None
        idiomDef.let_declarations = {'min': 1, 'max': 2}
        idiomDef.stores = 0
        return idiomDef


    def _getLetDeclarations(self):
        if len(self.idiom.let_declarations) <= 1:
            return ""

        decls = ""
        for decl in self.idiom.let_declarations:
            decls += f"                {decl.var_type} {decl.var_name};\n"
        return decls

    def _getDRAMReadIntrinsics(self):
        sendDramIntrinsics = ""
        arrayType = None
        for i, decl in enumerate(self.idiom.let_declarations):
            if decl.parsed_source:
                arrayAccess = decl.parsed_source
                sendDramIntrinsics += (f"{' ' * 20}send_dram_read({arrayAccess.array_name}+"
                                       f"{arrayAccess.index.constant_value}*sizeof({decl.var_type}), 1, "
                                       f"read_return_{arrayAccess.array_name}{i});\n")
                arrayType = decl.var_type
        return sendDramIntrinsics, arrayType

    def _genReadReturns(self, readCounter):
        res = ""
        for i, decl in enumerate(self.idiom.let_declarations):
            if decl.parsed_source:
                arrayAccess = decl.parsed_source
                if readCounter == 1:
                    res += f"""
                        event read_return_{arrayAccess.array_name}{i}({decl.var_type} {decl.var_name}) {{
                            
                            // In-Block
                            {self._getInBlock()}
                                
                            // Exit
                            {self.getTerminate(shouldYieldTerminate=True)}
                        }}
                    """
                else:
                    res += f"""
                        event read_return_{arrayAccess.array_name}{i}({decl.var_type} _{decl.var_name}) {{
                            {decl.var_name} = _{decl.var_name};
                            readCounter--;
                            if(readCounter == 0) {{
                                // In-Block
                                {self._getInBlock()}
                                
                                // Exit
                                {self.getTerminate(shouldYieldTerminate=True)}
                            }}
                            // else, wait for more data
                        }}
                    """
        return res

    def _getInBlock(self) -> str:
        return self.idiom.in_body


    def generate(self) -> str:
        # create a unique thread module name
        self._createUniqueThreadName()

        # let declarations
        readCounter, readCounterDecl, readCounterInit = self.getReadCounter()
        letDecl = self._getLetDeclarations()
        sendDramIntrinsics, arrayType = self._getDRAMReadIntrinsics()
        self.getStartEventParams()

        res = f"""
            thread {self.thread_name} {{
            
                // Let Declarations
                {letDecl.strip()}
                
                {readCounterDecl}
                
                // Start event parameters
                {self.threadParamsDecl.strip()}

                event start({self.startEventParams}) {{
                    {readCounterInit.strip()}
                    {self.threadParamsInit.strip()}
                    
                    // the {readCounter} reads
                    {sendDramIntrinsics.strip()}
                }}
                """

        res += self._genReadReturns(readCounter)
        res += "}\n"  # end thread
        return res



class Array2ReadsReductionStaticLoop(WeaveIdiom):
    """
    Idiom for reading to arrays in a loop with a reduction operation. Example:
    ```
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
    ```
    """

    def __init__(self):
        super().__init__()
        self._maxIterationsInFlight: int = 1
        self._masterThreadGenerated: bool = False

    @classmethod
    def getName(cls) -> str:
        return "Array2ReadReductionStaticLoop"

    @classmethod
    def getDefinition(cls) -> IdiomDefinition:
        loopDef = IdiomLoopDefinition()
        loopDef.stride = 1
        loopDef.direction = IdiomLoopDefinition.LoopDirection.FORWARD
        loopDef.staticBounds = True

        idiomDef = IdiomDefinition()
        idiomDef.loop = loopDef
        idiomDef.let_declarations = {'min': 1, 'max': 2}
        idiomDef.stores = 0
        return idiomDef


    def _getLetDeclarations(self):

        if len(self.idiom.let_declarations) <= 1:
            return ""

        tempNames = self._getCombinedLetVarNames()
        decls = ""
        decl = self.idiom.let_declarations[0]
        for i in range(0, 8):
            decls += f"                {decl.var_type} {tempNames}{i};\n"
        return decls

    def _getCombinedLetVarNames(self):
        names = []
        for decl in self.idiom.let_declarations:
            if decl.parsed_source:
                names.append(decl.var_name)
        return "_".join(names)

    def _genReadReturns(self, readCounter: int, readCounterInit: str, remainder: int) -> str:

        if remainder == 0:
            return ""

        res = ""
        tempNames = self._getCombinedLetVarNames()
        loop = self.idiom.for_loop

        # filter out all non-array accesses
        letDecl = []
        for decl in self.idiom.let_declarations:
            if decl.parsed_source:
                letDecl.append(decl)

        nextIteration = remainder * self._maxIterationsInFlight if remainder >= 8 else remainder

        for i, decl in enumerate(letDecl):
            arrayAccess = decl.parsed_source
            if readCounter == 1:
                res += f"""
                    event read_return_{arrayAccess.array_name}{remainder}({decl.var_type} {decl.var_name}) {{
                        //print("Hello");
                        // In-Block
                        {self._getInBlock()}
                            
                        // Exit
                        {loop.var_name} = {loop.var_name} + {nextIteration};
                        {self._getExit(readCounterInit)}
                    }}
                """
            else:
                theOtherLetDecl: LetDeclaration = letDecl[1 - i]
                subs = {
                    decl.var_name: f"_{decl.var_name}{{i}}",
                    theOtherLetDecl.var_name : f"{tempNames}{{i}}"
                }

                indent = " " * 28
                sep = "\n" + indent
                res += f"""
                    event read_return_{arrayAccess.array_name}{remainder}({', '.join([f"{decl.var_type} _{decl.var_name}{i}" for i in range(0, remainder)])}) {{
                        //print("Hello");
                        readCounter--;
                        if(readCounter == 1) {{
                            {sep.join([f"{tempNames}{i} = _{decl.var_name}{i};" for i in range(0, remainder)])}
                            yield;
                        }}
                        if(readCounter == 0) {{
                            // In-Block
                            {self._unrollInBlock(unroll_factor=remainder, substitutions=subs, indent=indent).strip()}
                            //print("Current sum: %ld", sum);
                            
                            // Check for exit
                            {loop.var_name} = {loop.var_name} + {nextIteration};
                            {self._getExit(readCounterInit)}
                        }}
                    }}
                """
        return res

    def _getInBlock(self) -> str:
        return self.idiom.in_body

    def _getExit(self, readCounterInit) -> str:
        loop: ForLoopSpec = self.idiom.for_loop

        # Check, if the loop iterations are divisible by 8. If not, we need to add a
        # check to load the remaining elements. However, since we expect constant loop bounds,
        # we know exactly how many elements to load.
        loopStart = loop.start.constant_value
        loopEnd = loop.end.constant_value
        nIterations = loopEnd - loopStart
        remainder = nIterations % 8

        if remainder == 0:
            res = f"""
                if({loop.raw_condition}) {{
                    {self.getLoopBody(readCounterInit, 8)}
                    yield;
                }}
            """
        else:
            loopCondition = f"{loop.var_name} < {loopEnd - remainder}"
            res = f"""
                if({loopCondition}) {{
                    {self.getLoopBody(readCounterInit, 8)}
                    yield;
                }}
                if({loop.raw_condition}) {{
                    // Handle remaining {remainder} elements
                    {self.getLoopBody(readCounterInit, remainder)}
                    yield;
                }}
            """

        res += self.getTerminate(shouldYieldTerminate=not self._masterThreadGenerated)
        return res


    def _generateMasterStartEvent(self):
        # determine the number of arrays to read and the number of thread to start
        letDecl = []
        for decl in self.idiom.let_declarations:
                if decl.parsed_source:
                    letDecl.append(decl)
        if not self.idiom.max_requests_in_flight:
            return ""

        self._maxIterationsInFlight = self.idiom.max_requests_in_flight // len(letDecl)
        if self._maxIterationsInFlight == 1:
            return ""


        if not self.idiom.scratchpad_offset:
            errorMsg(
                f"Idiom in lines {self.idiom.start_line}-{self.idiom.end_line} requires a scratchpad offset "
                f"to handle max_requests_in_flight!\n"
            )
            return ""

        eventVars = self.startEventVars.split(',')
        loop: ForLoopSpec = self.idiom.for_loop


        if len(eventVars)+1 > 8:
            errorMsg(
                "Number of input parameters for the idiom in "
                f"lines {self.idiom.start_line}-{self.idiom.end_line} exceeds 8!\nParameters: {eventVars}\n"
            )

        res = f"""
            thread {self.thread_name} {{
                {self.threadParamsDecl.strip()}
                unsigned long threadCount;
                event start({self.startEventParams}) {{
                    //print("Starting master thread with max iterations in flight: {self._maxIterationsInFlight}");
                    {self.threadParamsInit.strip()}
                    unsigned long evw = evw_new(NETID, {self.thread_name}_worker::start);
                    unsigned long cont = evw_update_event(CEVNT, doneAllThreads);
        """

        if len(eventVars)+1 > 3:
            res += f"unsigned long* local spPtr = LMBASE + {self.idiom.scratchpad_offset};\n"
            res += f"copyOperands(_{eventVars[0]}, spPtr, {len(eventVars)});\n"
            res += f"for(unsigned long threadStart=0; threadStart < {self._maxIterationsInFlight}; threadStart++) {{\n"
            res += f"    spPtr[{len(eventVars)}] = {loop.start.constant_value} + threadStart * 8;\n"
            res += f"    send_event(evw, spPtr, {len(eventVars)+1}, cont);\n"
            res += "}\n"
        else:
            res += f"for(unsigned long threadStart=0; threadStart < {self._maxIterationsInFlight}; threadStart++) {{\n"
            res += f"    send_event(evw, {self.startEventVars}, ({loop.start.constant_value} + threadStart * 8), cont);\n"
            res += "}\n"

        res += f"threadCount = {self._maxIterationsInFlight};\n"

        res += "}\n\n"  # end start event

        # The final event, perform the reduction here
        reductions = ""
        for red in self.idiom.reductions:
            reductions += f"{red.variable} = {red.variable} {red.operator} _{red.variable};\n"

        args = []
        onComplete : OnCompleteSpec = self.idiom.on_complete
        depsVarTypes = self.idiom.get_dependencies()['reduction_var_types']
        if onComplete and len(onComplete.arguments) > 0:
            # get the type of the reduction variable
            for arg in onComplete.arguments:
                if depsVarTypes:
                    arg_type = depsVarTypes.get(arg, "long")
                    args.append(f"{' '.join(arg_type.qualifiers)} {arg_type.base_type} _{arg}")
                else:
                    args.append(f"long _{arg}")
        res += f"""
            event doneAllThreads({' ,'.join(args)}) {{
                threadCount--;
                {reductions}
                if(threadCount == 0) {{
                    {self.getTerminate(shouldYieldTerminate=True)}
                }}
            }}
        """

        res += "}\n"  # end thread

        self._masterThreadGenerated = True
        return res


    def _generateWorkerThread(self) -> str:
        readCounter, readCounterDecl, readCounterInit = self.getReadCounter()
        letDecl = self._getLetDeclarations()
        loopDecl, loopInit = self.getLoopIterator()

        loop: ForLoopSpec = self.idiom.for_loop
        nElements = loop.end.constant_value - loop.start.constant_value
        remainder = nElements % 8
        if nElements < 8:
            sendDRAMRequest = self.getLoopBody(readCounterInit, nElements)
        else:
            sendDRAMRequest = self.getLoopBody(readCounterInit, 8)

        # create a master thread to start multiple threads if needed based on the max requests in flight

        if self._masterThreadGenerated:
            startParams = self.startEventParams + f", {' '.join(loop.var_qualifiers)} {loop.var_type} loop_start"
            loopInit = f"{loop.var_name} = loop_start;"
            workerThreadName = self.thread_name + "_worker"
        else:
            startParams = self.startEventParams
            workerThreadName = self.thread_name


        res = f"""
            thread {workerThreadName} {{
            
                // Let Declarations
                {letDecl.strip()}
                
                {readCounterDecl}
                
                // Start event parameters
                {self.threadParamsDecl.strip()}
                
                // Loop iterator
                {loopDecl.strip()}

                event start({startParams}) {{
                    //print("Starting worker thread");
                    {self.threadParamsInit.strip()}
                    {loopInit.strip()}
                    
                    {sendDRAMRequest}
                }}
                """

        res += self._genReadReturns(readCounter, readCounterInit, 8)
        res += self._genReadReturns(readCounter, readCounterInit, remainder)
        res += "}"
        return res

    def generate(self) -> str:
        self._createUniqueThreadName()
        self.getStartEventParams()
        res = self._generateMasterStartEvent()
        res += self._generateWorkerThread()
        return res


class Array2ReadsReductionDynamicLoop(Array2ReadsReductionStaticLoop):
    """
    Idiom for reading to arrays in a loop with a reduction operation. Example:
    ```
    event e(long* myArrayA, long* myArrayB) {
		long sum = 0;
		#pragma for reduction(+, sum) onComplete(eventOnComplete, sum)
		for(unsigned long i=0; i<nElements; i++) {
			Let {
				long a = myArrayA[i];
				long b = myArrayB[i];
			}
			In {
				sum = sum + a * b;
			}
		}
	}
    ```
    """

    @classmethod
    def getName(cls) -> str:
        return "Array2ReadReductionDynamicLoop"

    @classmethod
    def getDefinition(cls) -> IdiomDefinition:
        idiomDef: IdiomDefinition = Array2ReadsReductionStaticLoop.getDefinition()
        idiomDef.loop.staticBounds = False
        idiomDef.needsScratchpadOffset = True
        return idiomDef

    def _genReadReturns(self, readCounter: int, readCounterInit: str, remainder: int) -> str:

        if remainder == 0:
            return ""

        res = ""
        loop: ForLoopSpec = self.idiom.for_loop

        # filter out all non-array accesses
        letDecl = []
        for decl in self.idiom.let_declarations:
            if decl.parsed_source:
                letDecl.append(decl)

        nextIteration = remainder * self._maxIterationsInFlight if remainder >= 8 else remainder

        for i, decl in enumerate(letDecl):
            arrayAccess = decl.parsed_source
            if readCounter == 1:
                res += f"""
                    event read_return_{arrayAccess.array_name}{remainder}({decl.var_type} {decl.var_name}) {{
                        //print("Hello");
                        // In-Block
                        {self._getInBlock()}
                            
                        // Exit
                        {loop.var_name} = {loop.var_name} + {nextIteration};
                        {self._getExit(readCounterInit)}
                    }}
                """
            else:
                theOtherLetDecl: LetDeclaration = letDecl[1 - i]
                subs = {
                    decl.var_name: f"_{decl.var_name}{{i}}",
                    theOtherLetDecl.var_name : f"spPtr[{{i}}]"
                }

                indent = " " * 28
                res += f"""
                    event read_return_{arrayAccess.array_name}{remainder}({', '.join([f"{decl.var_type} _{decl.var_name}{i}" for i in range(0, remainder)])}) {{
                        //print("Hello");
                        readCounter--;
                        {decl.var_type}* local spPtr = LMBASE + {self.idiom.scratchpad_offset};
                        
                        if(readCounter == 1) {{
                            copyOperands(_{decl.var_name}0, spPtr, {remainder});
                            yield;
                        }}
                        if(readCounter == 0) {{
                            // In-Block
                            {self._unrollInBlock(unroll_factor=remainder, substitutions=subs, indent=indent).strip()}
                            
                            // Check for exit
                            {loop.var_name} = {loop.var_name} + {nextIteration};
                            {self._getExit(readCounterInit)}
                        }}
                    }}
                """
        return res

    def _getExit(self, readCounterInit) -> str:
        loop: ForLoopSpec = self.idiom.for_loop

        res = f"""
            unsigned long remainingElements = {loop.end.raw_expr} - {loop.var_name};

            if(remainingElements >= 8) {{
                {self.getLoopBody(readCounterInit, 8)}
            }} elif(remainingElements == 7) {{
                {self.getLoopBody(readCounterInit, 7)}
            }} elif(remainingElements == 6) {{
                {self.getLoopBody(readCounterInit, 6)}
            }} elif(remainingElements == 5) {{
                {self.getLoopBody(readCounterInit, 5)}
            }} elif(remainingElements == 4) {{
                {self.getLoopBody(readCounterInit, 4)}
            }} elif(remainingElements == 3) {{
                {self.getLoopBody(readCounterInit, 3)}
            }} elif(remainingElements == 2) {{
                {self.getLoopBody(readCounterInit, 2)}
            }} elif(remainingElements == 1) {{
                {self.getLoopBody(readCounterInit, 1)}
            }} else {{
                {self.getTerminate(shouldYieldTerminate=True)}
            }}
"""
        return res


    def generate(self) -> str:
        self._createUniqueThreadName()

        readCounter, readCounterDecl, readCounterInit = self.getReadCounter()
        self.getStartEventParams()
        loopDecl, loopInit = self.getLoopIterator()

        loop: ForLoopSpec = self.idiom.for_loop

        res = f"""
            thread {self.thread_name} {{

                {readCounterDecl}

                // Start event parameters
                {self.threadParamsDecl.strip()}

                // Loop iterator
                {loopDecl.strip()}

                event start({self.startEventParams}) {{
                    {self.threadParamsInit.strip()}
                    {loopInit.strip()}

                    unsigned long remainingElements = {loop.end.raw_expr} - {loop.start.raw_expr};

                    if(remainingElements >= 8) {{
                        {self.getLoopBody(readCounterInit, 8)}
                    }} elif(remainingElements == 7) {{
                        {self.getLoopBody(readCounterInit, 7)}
                    }} elif(remainingElements == 6) {{
                        {self.getLoopBody(readCounterInit, 6)}
                    }} elif(remainingElements == 5) {{
                        {self.getLoopBody(readCounterInit, 5)}
                    }} elif(remainingElements == 4) {{
                        {self.getLoopBody(readCounterInit, 4)}
                    }} elif(remainingElements == 3) {{
                        {self.getLoopBody(readCounterInit, 3)}
                    }} elif(remainingElements == 2) {{
                        {self.getLoopBody(readCounterInit, 2)}
                    }} elif(remainingElements == 1) {{
                        {self.getLoopBody(readCounterInit, 1)}
                    }} else {{
                        {self.getTerminate(shouldYieldTerminate=True)}
                    }}
                }}
                """

        for i in range(1, 9):
            res += self._genReadReturns(readCounter, readCounterInit, i)
        res += "}"
        return res


class Array1Read1WriteStaticLoop(Array2ReadsReductionStaticLoop):
    """
    Idiom for reading ome array and writing to one array. Example:
    ```
    event e(long* myArrayA, long* myArrayB) {
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
    ```
    """

    @classmethod
    def getName(cls) -> str:
        return "Array1Read1WriteStaticLoop"

    @classmethod
    def getDefinition(cls) -> IdiomDefinition:
        loopDef = IdiomLoopDefinition()
        loopDef.stride = 1
        loopDef.direction = IdiomLoopDefinition.LoopDirection.FORWARD

        idiomDef = IdiomDefinition()
        idiomDef.loop = loopDef
        idiomDef.let_declarations = {'min': 1, 'max': 1}
        idiomDef.stores = 1
        return idiomDef


    def _genReadReturns(self, readCounter: int, readCounterInit: str, remainder: int) -> str:

        if remainder == 0:
            return ""

        loop: ForLoopSpec = self.idiom.for_loop

        # filter out all non-array accesses
        letDecl = []
        for decl in self.idiom.let_declarations:
            if decl.parsed_source:
                letDecl.append(decl)

        # we expect only 1 array load
        decl = letDecl[0]
        arrayAccess = decl.parsed_source

        # store operations
        storeOps: List[StoreOperation] = self.idiom.store_operations
        instructions = []
        for storeOp in storeOps:
            instructions.append(f"{' '.join(decl.qualifiers)} {decl.var_type}* {storeOp.array_name}Local"
                                    f" = (readAddress - {arrayAccess.array_name}) + {storeOp.array_name};")
            instructions.append(f"//print(\"Hello: %ld WA: 0x%lx\", i, {storeOps[0].array_name}Local);")
            instructions.append(f"send_dram_write_ops({storeOp.array_name}Local, _{decl.var_name}0, "
                             f"{remainder}, write_return_{storeOp.array_name});")

        indent = "\n" + (" " * 16)
        parametersText = ', '.join([f"{decl.var_type} _{decl.var_name}{i}" for i in range(0, remainder)])
        res = f"""
            event read_return_{arrayAccess.array_name}{remainder}({parametersText}, unsigned long* readAddress) {{
                {indent.join(instructions)}
                writeCounter++;
                
                // Send more reads
        """

        loopStart = loop.start.constant_value
        loopEnd = loop.end.constant_value
        nIterations = loopEnd - loopStart
        remainderLocal = nIterations % 8
        if remainderLocal == 0:
            res += f"""
                if({loop.raw_condition}) {{
                    {self.getLoopBody("", 8)}
                    yield;
                }}
            """
        else:
            loopCondition = f"{loop.var_name} {loop.comparison_op} {loopEnd - remainderLocal}"
            res += f"""
                if({loopCondition}) {{
                    {self.getLoopBody("", 8)}
                    {loop.var_name} = {loop.var_name} + 8;
                    //print("READ WC %ld RC %ld i: %ld", writeCounter, readCounter, i);
                    yield;
                }}
                if({loop.raw_condition}) {{
                    // Handle remaining {remainderLocal} elements
                    {self.getLoopBody("", remainderLocal)}
                    {loop.var_name} = {loop.var_name} + {remainderLocal};
                    //print("READ WC %ld RC %ld i: %ld", writeCounter, readCounter, i);
                    yield;
                }}
                readCounter--;
            """
        res += "}\n"
        return res

    def _genWriteReturns(self) -> str:
        res = ""
        storeOps: List[StoreOperation] = self.idiom.store_operations
        loop: ForLoopSpec = self.idiom.for_loop

        for storeOp in storeOps:
            res += f"""
                event write_return_{storeOp.array_name}() {{
                    //print("Hello WC %ld RC %ld i: %ld", writeCounter, readCounter, i);
                    writeCounter--;
                    if(writeCounter == 0 && readCounter == 0) {{
                        // Exit
                        {self.getTerminate(shouldYieldTerminate=True)}
                    }}
                    // else, wait for more writes
                }}
            """
        return res

    def generate(self) -> str:
        self._createUniqueThreadName()

        readCounter, readCounterDecl, readCounterInit = self.getReadCounter(init=0, threshold=1)
        letDecl = self._getLetDeclarations()
        self.getStartEventParams()
        loopDecl, loopInit = self.getLoopIterator()

        loop: ForLoopSpec = self.idiom.for_loop
        nElements = loop.end.constant_value - loop.start.constant_value

        # find the array access in the Let declarations
        arrayAccess = None
        for ld in self.idiom.let_declarations:
            if ld.parsed_source:
                arrayAccess = ld
                break

        if not arrayAccess:
            errorMsg("No array access found in Let declarations in idiom in "
                    f"lines {self.idiom.start_line}-{self.idiom.end_line}!\n")

        sendDRAMRequest = ""
        if nElements < 8:
            sendDRAMRequest = self.getLoopBody("readCounter = 1;", nElements)
        else:
            if self.idiom.max_requests_in_flight:
                maxInFlightRead = self.idiom.max_requests_in_flight // 2  # each iteration has 1 read and 1 write
                if maxInFlightRead == 0:
                    errorMsg("maxRequestsInFlight is too small to handle read and write requests in idiom in "
                             f"lines {self.idiom.start_line}-{self.idiom.end_line}!\n")

                maxInFlightRead = min(maxInFlightRead, nElements // 8)
                sendDRAMRequest += f"readCounter = {maxInFlightRead};\n"
                sendDRAMRequest += (f"\t{' '.join(arrayAccess.qualifiers)} {arrayAccess.var_type}* "
                                    f"{arrayAccess.parsed_source.array_name}Local = "
                                    f"{arrayAccess.parsed_source.array_name} + "
                                    f"({loop.var_name}*sizeof({arrayAccess.var_type}));\n")

                sendDRAMRequest += f"for(unsigned long readReq=0; readReq<{maxInFlightRead}; readReq++) {{\n"
                sendDRAMRequest += f"\t//print(\"%ld, RA: 0x%lx\", i, {arrayAccess.parsed_source.array_name}Local);\n"
                sendDRAMRequest += (f"\tsend_dram_read({arrayAccess.parsed_source.array_name}Local, 8, "
                                    f"read_return_{arrayAccess.parsed_source.array_name}{8});\n")
                sendDRAMRequest += (f"\t{arrayAccess.parsed_source.array_name}Local = "
                                    f"{arrayAccess.parsed_source.array_name}Local + 64;\n")
                sendDRAMRequest += f"}}\n"

                sendDRAMRequest += f"\n{loop.var_name} = {loop.var_name} + {maxInFlightRead * 8};\n"
            else:
                sendDRAMRequest = self.getLoopBody("", 8)

        res = f"""
            thread {self.thread_name} {{
            
                // Let Declarations
                {letDecl.strip()}
                
                // Store Management Declarations
                unsigned long writeCounter;
                {readCounterDecl}
                
                // Start event parameters
                {self.threadParamsDecl.strip()}
                
                // Loop iterator
                {loopDecl.strip()}

                event start({self.startEventParams}) {{
                    //print("Starting idiom {self.getName()} %ld", i);
                    {self.threadParamsInit.strip()}
                    {loopInit.strip()}
                    writeCounter = 0;
                    
                    {sendDRAMRequest}
                }}
                """

        remainder = nElements % 8
        res += self._genReadReturns(readCounter, readCounterInit, 8)
        res += self._genReadReturns(readCounter, readCounterInit, remainder)
        res += self._genWriteReturns()
        res += "}"
        return res



class Array1Read1WriteDynamicLoop(Array2ReadsReductionStaticLoop):
    """
    Idiom for reading ome array and writing to one array. Example:
    ```
    event e(long* myArrayA, long* myArrayB, unsigned long nElements) {
		#pragma for onComplete(eventOnComplete)
		for(unsigned long i=0; i<nElements; i++) {
			Let {
				long a = myArrayA[i];
			}
			In {
				myArrayB[i] = a;
			}
		}
	}
    ```
    """


    @classmethod
    def getName(cls) -> str:
        return "Array1Read1WriteDynamicLoop"


    @classmethod
    def getDefinition(cls) -> IdiomDefinition:
        idiomDef = Array1Read1WriteStaticLoop.getDefinition()
        idiomDef.loop.staticBounds = False
        return idiomDef


    def _genReadReturns(self, readCounter: int, readCounterInit: str, remainder: int) -> str:

        if remainder == 0:
            return ""

        loop: ForLoopSpec = self.idiom.for_loop

        # filter out all non-array accesses
        letDecl = []
        for decl in self.idiom.let_declarations:
            if decl.parsed_source:
                letDecl.append(decl)

        # we expect only 1 array load
        decl = letDecl[0]
        arrayAccess = decl.parsed_source

        # store operations
        storeOps: List[StoreOperation] = self.idiom.store_operations
        instructions = []
        for storeOp in storeOps:
            instructions.append(f"{' '.join(decl.qualifiers)} {decl.var_type}* {storeOp.array_name}Local"
                                    f" = (readAddress - {arrayAccess.array_name}) + {storeOp.array_name};")
            instructions.append(f"//print(\"Hello: %ld WA: 0x%lx\", i, {storeOps[0].array_name}Local);")
            instructions.append(f"send_dram_write_ops({storeOp.array_name}Local, _{decl.var_name}0, "
                             f"{remainder}, write_return_{storeOp.array_name});")

        indent = "\n" + (" " * 16)
        parametersText = ', '.join([f"{decl.var_type} _{decl.var_name}{i}" for i in range(0, remainder)])
        res = f"""
            event read_return_{arrayAccess.array_name}{remainder}({parametersText}, unsigned long* readAddress) {{
                {indent.join(instructions)}
                writeCounter++;
                
                // Send more reads
                unsigned long remainingElements = {loop.end.raw_expr} - {loop.var_name};
                //print("READ WC %ld RC %ld i: %ld, remainingElements: %lu, WA: 0x%lx, RA: 0x%lx", writeCounter, readCounter, i, remainingElements, myArrayBLocal, readAddress);
                if(remainingElements >= 8) {{
                    {self.getLoopBody("", 8)}
                    {loop.var_name} = {loop.var_name} + 8;
                }} elif(remainingElements == 7) {{
                    {self.getLoopBody("", 7)}
                    {loop.var_name} = {loop.var_name} + 7;
                }} elif(remainingElements == 6) {{
                    {self.getLoopBody("", 6)}
                    {loop.var_name} = {loop.var_name} + 6;
                }} elif(remainingElements == 5) {{
                    {self.getLoopBody("", 5)}
                    {loop.var_name} = {loop.var_name} + 5;
                }} elif(remainingElements == 4) {{
                    {self.getLoopBody("", 4)}
                    {loop.var_name} = {loop.var_name} + 4;
                }} elif(remainingElements == 3) {{
                    {self.getLoopBody("", 3)}
                    {loop.var_name} = {loop.var_name} + 3;
                }} elif(remainingElements == 2) {{
                    {self.getLoopBody("", 2)}
                    {loop.var_name} = {loop.var_name} + 2;
                }} elif(remainingElements == 1) {{
                    {self.getLoopBody("", 1)}
                    {loop.var_name} = {loop.var_name} + 1;
                }} else {{
                    readCounter--; // one less read
                }}
        """
        res += "}\n"
        return res

    def _genWriteReturns(self) -> str:
        res = ""
        storeOps: List[StoreOperation] = self.idiom.store_operations
        loop: ForLoopSpec = self.idiom.for_loop

        for storeOp in storeOps:
            res += f"""
                event write_return_{storeOp.array_name}() {{
                    //print("Hello WC %ld RC %ld i: %ld", writeCounter, readCounter, i);
                    writeCounter--;
                    if(writeCounter == 0 && readCounter == 0) {{
                        // Exit
                        {self.getTerminate(shouldYieldTerminate=True)}
                    }}
                    // else, wait for more writes
                }}
            """
        return res

    def generate(self) -> str:
        self._createUniqueThreadName()

        readCounter, readCounterDecl, readCounterInit = self.getReadCounter(init=0, threshold=1)
        letDecl = self._getLetDeclarations()
        self.getStartEventParams()
        loopDecl, loopInit = self.getLoopIterator()

        loop: ForLoopSpec = self.idiom.for_loop

        # find the array access in the Let declarations
        arrayAccess = None
        for ld in self.idiom.let_declarations:
            if ld.parsed_source:
                arrayAccess = ld
                break

        if not arrayAccess:
            errorMsg("No array access found in Let declarations in idiom in "
                    f"lines {self.idiom.start_line}-{self.idiom.end_line}!\n")

        maxRequestLoop = ["", ""]
        if self.idiom.max_requests_in_flight:
            # 1 read and 1 write = 2 requests in flight
            maxRequestLoop[0] = f"for(unsigned long readReq=0; readReq<{self.idiom.max_requests_in_flight // 2}; readReq++) {{\n"
            maxRequestLoop[1] = "}\n"

        res = f"""
            thread {self.thread_name} {{
            
                // Let Declarations
                {letDecl.strip()}
                
                // Store Management Declarations
                unsigned long writeCounter;
                {readCounterDecl}
                
                // Start event parameters
                {self.threadParamsDecl.strip()}
                
                // Loop iterator
                {loopDecl.strip()}

                event start({self.startEventParams}) {{
                    //print("Starting idiom {self.getName()} %ld", i);
                    {self.threadParamsInit.strip()}
                    {loopInit.strip()}
                    writeCounter = 0;
                    readCounter = 0;
                    
                    
                    {maxRequestLoop[0]}
                        unsigned long remainingElements = {loop.end.raw_expr} - {loop.var_name};
                        
                        if(remainingElements >= 8) {{
                            {self.getLoopBody("readCounter++;", 8)}
                            {loop.var_name} = {loop.var_name} + 8;
                        }} elif(remainingElements == 7) {{
                            {self.getLoopBody("readCounter++;", 7)}
                            {loop.var_name} = {loop.var_name} + 7;
                        }} elif(remainingElements == 6) {{
                            {self.getLoopBody("readCounter++;", 6)}
                            {loop.var_name} = {loop.var_name} + 6;
                        }} elif(remainingElements == 5) {{
                            {self.getLoopBody("readCounter++;", 5)}
                            {loop.var_name} = {loop.var_name} + 5;
                        }} elif(remainingElements == 4) {{
                            {self.getLoopBody("readCounter++;", 4)}
                            {loop.var_name} = {loop.var_name} + 4;
                        }} elif(remainingElements == 3) {{
                            {self.getLoopBody("readCounter++;", 3)}
                            {loop.var_name} = {loop.var_name} + 3;
                        }} elif(remainingElements == 2) {{
                            {self.getLoopBody("readCounter++;", 2)}
                            {loop.var_name} = {loop.var_name} + 2;
                        }} elif(remainingElements == 1) {{
                            {self.getLoopBody("readCounter++;", 1)}
                            {loop.var_name} = {loop.var_name} + 1;
                        }} else {{
                            break;
                        }}
                    {maxRequestLoop[1]}
                }}
                """

        for i in range(1, 9):
            res += self._genReadReturns(readCounter, readCounterInit, i)
        res += self._genWriteReturns()
        res += "}" # thread end
        return res