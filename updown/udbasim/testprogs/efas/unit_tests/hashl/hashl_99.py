from EFA_v2 import *
def hashl_99():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2733225053484253209, -3753393449519922785, -3322609536996334462]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 9710")
    tran0.writeAction("slorii X17 X17 12 1499")
    tran0.writeAction("slorii X17 X17 12 1140")
    tran0.writeAction("slorii X17 X17 12 520")
    tran0.writeAction("slorii X17 X17 12 25")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 52201")
    tran0.writeAction("slorii X17 X17 12 1096")
    tran0.writeAction("slorii X17 X17 12 2883")
    tran0.writeAction("slorii X17 X17 12 356")
    tran0.writeAction("slorii X17 X17 12 415")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 53731")
    tran0.writeAction("slorii X17 X17 12 2947")
    tran0.writeAction("slorii X17 X17 12 2788")
    tran0.writeAction("slorii X17 X17 12 34")
    tran0.writeAction("slorii X17 X17 12 1154")
    tran0.writeAction("hashl X16 X17 2")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
