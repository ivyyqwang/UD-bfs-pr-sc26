from EFA_v2 import *
def add_84():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3142292282240706548, 3654192337242625479]
    tran0.writeAction("movir X16 54372")
    tran0.writeAction("slorii X16 X16 12 1373")
    tran0.writeAction("slorii X16 X16 12 352")
    tran0.writeAction("slorii X16 X16 12 2421")
    tran0.writeAction("slorii X16 X16 12 2060")
    tran0.writeAction("movir X17 12982")
    tran0.writeAction("slorii X17 X17 12 1225")
    tran0.writeAction("slorii X17 X17 12 490")
    tran0.writeAction("slorii X17 X17 12 1233")
    tran0.writeAction("slorii X17 X17 12 1479")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
