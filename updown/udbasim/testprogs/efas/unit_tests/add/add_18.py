from EFA_v2 import *
def add_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7767583504600536530, 8975352777125828857]
    tran0.writeAction("movir X16 37939")
    tran0.writeAction("slorii X16 X16 12 4095")
    tran0.writeAction("slorii X16 X16 12 1277")
    tran0.writeAction("slorii X16 X16 12 414")
    tran0.writeAction("slorii X16 X16 12 2606")
    tran0.writeAction("movir X17 31886")
    tran0.writeAction("slorii X17 X17 12 3516")
    tran0.writeAction("slorii X17 X17 12 3102")
    tran0.writeAction("slorii X17 X17 12 1641")
    tran0.writeAction("slorii X17 X17 12 2297")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
