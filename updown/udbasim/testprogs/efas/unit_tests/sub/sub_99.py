from EFA_v2 import *
def sub_99():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3137903364402009194, 1829739136180943875]
    tran0.writeAction("movir X16 54387")
    tran0.writeAction("slorii X16 X16 12 3800")
    tran0.writeAction("slorii X16 X16 12 1009")
    tran0.writeAction("slorii X16 X16 12 1290")
    tran0.writeAction("slorii X16 X16 12 2966")
    tran0.writeAction("movir X17 6500")
    tran0.writeAction("slorii X17 X17 12 2208")
    tran0.writeAction("slorii X17 X17 12 3275")
    tran0.writeAction("slorii X17 X17 12 2847")
    tran0.writeAction("slorii X17 X17 12 3075")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
