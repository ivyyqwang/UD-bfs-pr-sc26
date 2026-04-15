from EFA_v2 import *
def srsubii_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [140625208900421813, 4, 143]
    tran0.writeAction("movir X16 499")
    tran0.writeAction("slorii X16 X16 12 2462")
    tran0.writeAction("slorii X16 X16 12 486")
    tran0.writeAction("slorii X16 X16 12 3992")
    tran0.writeAction("slorii X16 X16 12 2229")
    tran0.writeAction("srsubii X16 X17 4 143")
    tran0.writeAction("yieldt")
    return efa
