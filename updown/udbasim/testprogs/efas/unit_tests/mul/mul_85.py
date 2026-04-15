from EFA_v2 import *
def mul_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8001409117435553487, -6553956055478531891]
    tran0.writeAction("movir X16 28426")
    tran0.writeAction("slorii X16 X16 12 2931")
    tran0.writeAction("slorii X16 X16 12 755")
    tran0.writeAction("slorii X16 X16 12 1302")
    tran0.writeAction("slorii X16 X16 12 1743")
    tran0.writeAction("movir X17 42251")
    tran0.writeAction("slorii X17 X17 12 2747")
    tran0.writeAction("slorii X17 X17 12 287")
    tran0.writeAction("slorii X17 X17 12 2792")
    tran0.writeAction("slorii X17 X17 12 2253")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
