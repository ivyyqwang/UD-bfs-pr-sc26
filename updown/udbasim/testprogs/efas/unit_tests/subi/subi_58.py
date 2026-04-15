from EFA_v2 import *
def subi_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8155073150107590410, -18583]
    tran0.writeAction("movir X16 36563")
    tran0.writeAction("slorii X16 X16 12 1474")
    tran0.writeAction("slorii X16 X16 12 3434")
    tran0.writeAction("slorii X16 X16 12 2094")
    tran0.writeAction("slorii X16 X16 12 246")
    tran0.writeAction("subi X16 X17 -18583")
    tran0.writeAction("yieldt")
    return efa
