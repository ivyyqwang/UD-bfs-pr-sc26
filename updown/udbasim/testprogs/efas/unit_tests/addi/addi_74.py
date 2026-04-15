from EFA_v2 import *
def addi_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7326232215823363830, 25641]
    tran0.writeAction("movir X16 26028")
    tran0.writeAction("slorii X16 X16 12 22")
    tran0.writeAction("slorii X16 X16 12 606")
    tran0.writeAction("slorii X16 X16 12 714")
    tran0.writeAction("slorii X16 X16 12 3830")
    tran0.writeAction("addi X16 X17 25641")
    tran0.writeAction("yieldt")
    return efa
