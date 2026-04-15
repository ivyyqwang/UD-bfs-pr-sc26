from EFA_v2 import *
def add_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8892113816821448137, 5571209336697632517]
    tran0.writeAction("movir X16 33944")
    tran0.writeAction("slorii X16 X16 12 3545")
    tran0.writeAction("slorii X16 X16 12 2198")
    tran0.writeAction("slorii X16 X16 12 60")
    tran0.writeAction("slorii X16 X16 12 567")
    tran0.writeAction("movir X17 19792")
    tran0.writeAction("slorii X17 X17 12 3733")
    tran0.writeAction("slorii X17 X17 12 4043")
    tran0.writeAction("slorii X17 X17 12 827")
    tran0.writeAction("slorii X17 X17 12 1797")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
