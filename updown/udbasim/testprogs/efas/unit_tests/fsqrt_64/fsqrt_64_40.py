from EFA_v2 import *
def fsqrt_64_40():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12665234449797055975]
    tran0.writeAction("movir X16 44995")
    tran0.writeAction("slorii X16 X16 12 3898")
    tran0.writeAction("slorii X16 X16 12 249")
    tran0.writeAction("slorii X16 X16 12 792")
    tran0.writeAction("slorii X16 X16 12 1511")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
