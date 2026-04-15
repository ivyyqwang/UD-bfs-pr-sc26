from EFA_v2 import *
def srsubii_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2285703091564421302, 2, 1554]
    tran0.writeAction("movir X16 8120")
    tran0.writeAction("slorii X16 X16 12 1837")
    tran0.writeAction("slorii X16 X16 12 2562")
    tran0.writeAction("slorii X16 X16 12 2906")
    tran0.writeAction("slorii X16 X16 12 182")
    tran0.writeAction("srsubii X16 X17 2 1554")
    tran0.writeAction("yieldt")
    return efa
