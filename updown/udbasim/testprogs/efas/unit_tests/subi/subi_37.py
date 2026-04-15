from EFA_v2 import *
def subi_37():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1320024532014847657, 25823]
    tran0.writeAction("movir X16 60846")
    tran0.writeAction("slorii X16 X16 12 1354")
    tran0.writeAction("slorii X16 X16 12 3730")
    tran0.writeAction("slorii X16 X16 12 1858")
    tran0.writeAction("slorii X16 X16 12 2391")
    tran0.writeAction("subi X16 X17 25823")
    tran0.writeAction("yieldt")
    return efa
