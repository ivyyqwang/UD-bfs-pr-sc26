from EFA_v2 import *
def fsqrt_64_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14889535154098578095]
    tran0.writeAction("movir X16 52898")
    tran0.writeAction("slorii X16 X16 12 1045")
    tran0.writeAction("slorii X16 X16 12 1442")
    tran0.writeAction("slorii X16 X16 12 3018")
    tran0.writeAction("slorii X16 X16 12 687")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
