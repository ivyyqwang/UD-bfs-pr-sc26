from EFA_v2 import *
def div_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6102511725604167772, -4013825088986836164]
    tran0.writeAction("movir X16 21680")
    tran0.writeAction("slorii X16 X16 12 1953")
    tran0.writeAction("slorii X16 X16 12 1274")
    tran0.writeAction("slorii X16 X16 12 1198")
    tran0.writeAction("slorii X16 X16 12 92")
    tran0.writeAction("movir X17 51276")
    tran0.writeAction("slorii X17 X17 12 117")
    tran0.writeAction("slorii X17 X17 12 2308")
    tran0.writeAction("slorii X17 X17 12 1593")
    tran0.writeAction("slorii X17 X17 12 828")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
