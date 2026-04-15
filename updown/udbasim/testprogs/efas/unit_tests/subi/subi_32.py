from EFA_v2 import *
def subi_32():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6975127837723742145, 31874]
    tran0.writeAction("movir X16 24780")
    tran0.writeAction("slorii X16 X16 12 2589")
    tran0.writeAction("slorii X16 X16 12 6")
    tran0.writeAction("slorii X16 X16 12 1892")
    tran0.writeAction("slorii X16 X16 12 4033")
    tran0.writeAction("subi X16 X17 31874")
    tran0.writeAction("yieldt")
    return efa
