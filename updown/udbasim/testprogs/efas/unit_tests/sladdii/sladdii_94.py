from EFA_v2 import *
def sladdii_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6409816439516679435, 4, 1467]
    tran0.writeAction("movir X16 42763")
    tran0.writeAction("slorii X16 X16 12 3102")
    tran0.writeAction("slorii X16 X16 12 2223")
    tran0.writeAction("slorii X16 X16 12 611")
    tran0.writeAction("slorii X16 X16 12 757")
    tran0.writeAction("sladdii X16 X17 4 1467")
    tran0.writeAction("yieldt")
    return efa
