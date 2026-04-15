from EFA_v2 import *
def sladdii_34():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5636519378482197220, 5, 31]
    tran0.writeAction("movir X16 45511")
    tran0.writeAction("slorii X16 X16 12 247")
    tran0.writeAction("slorii X16 X16 12 3363")
    tran0.writeAction("slorii X16 X16 12 3944")
    tran0.writeAction("slorii X16 X16 12 3356")
    tran0.writeAction("sladdii X16 X17 5 31")
    tran0.writeAction("yieldt")
    return efa
