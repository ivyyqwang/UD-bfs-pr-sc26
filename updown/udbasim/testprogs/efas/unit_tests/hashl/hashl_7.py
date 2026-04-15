from EFA_v2 import *
def hashl_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8316554593435018534, 8725209085630496248, -438579672942825224]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 35989")
    tran0.writeAction("slorii X17 X17 12 2714")
    tran0.writeAction("slorii X17 X17 12 2311")
    tran0.writeAction("slorii X17 X17 12 665")
    tran0.writeAction("slorii X17 X17 12 2778")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 30998")
    tran0.writeAction("slorii X17 X17 12 694")
    tran0.writeAction("slorii X17 X17 12 3948")
    tran0.writeAction("slorii X17 X17 12 67")
    tran0.writeAction("slorii X17 X17 12 3576")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 63977")
    tran0.writeAction("slorii X17 X17 12 3489")
    tran0.writeAction("slorii X17 X17 12 3188")
    tran0.writeAction("slorii X17 X17 12 2195")
    tran0.writeAction("slorii X17 X17 12 248")
    tran0.writeAction("hashl X16 X17 2")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
