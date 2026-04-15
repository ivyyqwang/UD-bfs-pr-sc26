from EFA_v2 import *
def subi_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7239854863730496820, 31869]
    tran0.writeAction("movir X16 39814")
    tran0.writeAction("slorii X16 X16 12 3557")
    tran0.writeAction("slorii X16 X16 12 3101")
    tran0.writeAction("slorii X16 X16 12 3930")
    tran0.writeAction("slorii X16 X16 12 2764")
    tran0.writeAction("subi X16 X17 31869")
    tran0.writeAction("yieldt")
    return efa
