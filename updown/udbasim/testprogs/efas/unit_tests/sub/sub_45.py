from EFA_v2 import *
def sub_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1849212388163323815, -7602974832081997472]
    tran0.writeAction("movir X16 58966")
    tran0.writeAction("slorii X16 X16 12 1138")
    tran0.writeAction("slorii X16 X16 12 361")
    tran0.writeAction("slorii X16 X16 12 1119")
    tran0.writeAction("slorii X16 X16 12 2137")
    tran0.writeAction("movir X17 38524")
    tran0.writeAction("slorii X17 X17 12 3306")
    tran0.writeAction("slorii X17 X17 12 3113")
    tran0.writeAction("slorii X17 X17 12 2119")
    tran0.writeAction("slorii X17 X17 12 352")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
