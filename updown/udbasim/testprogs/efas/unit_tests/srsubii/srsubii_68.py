from EFA_v2 import *
def srsubii_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-481192129520760112, 6, 698]
    tran0.writeAction("movir X16 63826")
    tran0.writeAction("slorii X16 X16 12 1892")
    tran0.writeAction("slorii X16 X16 12 3779")
    tran0.writeAction("slorii X16 X16 12 824")
    tran0.writeAction("slorii X16 X16 12 2768")
    tran0.writeAction("srsubii X16 X17 6 698")
    tran0.writeAction("yieldt")
    return efa
