from EFA_v2 import *
def sladdii_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6722116710425132348, 6, 21]
    tran0.writeAction("movir X16 23881")
    tran0.writeAction("slorii X16 X16 12 3096")
    tran0.writeAction("slorii X16 X16 12 2151")
    tran0.writeAction("slorii X16 X16 12 2487")
    tran0.writeAction("slorii X16 X16 12 3388")
    tran0.writeAction("sladdii X16 X17 6 21")
    tran0.writeAction("yieldt")
    return efa
