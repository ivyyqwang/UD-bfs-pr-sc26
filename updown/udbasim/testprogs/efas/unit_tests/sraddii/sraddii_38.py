from EFA_v2 import *
def sraddii_38():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3635283923574008113, 6, 1763]
    tran0.writeAction("movir X16 52620")
    tran0.writeAction("slorii X16 X16 12 3592")
    tran0.writeAction("slorii X16 X16 12 2101")
    tran0.writeAction("slorii X16 X16 12 2797")
    tran0.writeAction("slorii X16 X16 12 1743")
    tran0.writeAction("sraddii X16 X17 6 1763")
    tran0.writeAction("yieldt")
    return efa
