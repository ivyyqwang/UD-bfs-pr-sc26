from EFA_v2 import *
def sladdii_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-9084529764894308258, 1, 733]
    tran0.writeAction("movir X16 33261")
    tran0.writeAction("slorii X16 X16 12 1092")
    tran0.writeAction("slorii X16 X16 12 3980")
    tran0.writeAction("slorii X16 X16 12 48")
    tran0.writeAction("slorii X16 X16 12 2142")
    tran0.writeAction("sladdii X16 X17 1 733")
    tran0.writeAction("yieldt")
    return efa
