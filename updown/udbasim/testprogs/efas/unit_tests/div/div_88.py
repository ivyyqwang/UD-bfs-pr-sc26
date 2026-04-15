from EFA_v2 import *
def div_88():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1586625756761672220, -187113333696792549]
    tran0.writeAction("movir X16 59899")
    tran0.writeAction("slorii X16 X16 12 708")
    tran0.writeAction("slorii X16 X16 12 2000")
    tran0.writeAction("slorii X16 X16 12 3011")
    tran0.writeAction("slorii X16 X16 12 1508")
    tran0.writeAction("movir X17 64871")
    tran0.writeAction("slorii X17 X17 12 982")
    tran0.writeAction("slorii X17 X17 12 2580")
    tran0.writeAction("slorii X17 X17 12 1079")
    tran0.writeAction("slorii X17 X17 12 2075")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
