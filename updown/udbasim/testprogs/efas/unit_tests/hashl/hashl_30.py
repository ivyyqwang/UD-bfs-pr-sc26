from EFA_v2 import *
def hashl_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8405325213099183217, 1575073661359841545, 7902893794050833691, -4518053119563496404]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 29861")
    tran0.writeAction("slorii X17 X17 12 2923")
    tran0.writeAction("slorii X17 X17 12 3964")
    tran0.writeAction("slorii X17 X17 12 1684")
    tran0.writeAction("slorii X17 X17 12 3185")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 5595")
    tran0.writeAction("slorii X17 X17 12 3218")
    tran0.writeAction("slorii X17 X17 12 1632")
    tran0.writeAction("slorii X17 X17 12 1750")
    tran0.writeAction("slorii X17 X17 12 265")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 28076")
    tran0.writeAction("slorii X17 X17 12 2944")
    tran0.writeAction("slorii X17 X17 12 2252")
    tran0.writeAction("slorii X17 X17 12 159")
    tran0.writeAction("slorii X17 X17 12 3355")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 49484")
    tran0.writeAction("slorii X17 X17 12 2666")
    tran0.writeAction("slorii X17 X17 12 28")
    tran0.writeAction("slorii X17 X17 12 296")
    tran0.writeAction("slorii X17 X17 12 1068")
    tran0.writeAction("hashl X16 X17 3")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
