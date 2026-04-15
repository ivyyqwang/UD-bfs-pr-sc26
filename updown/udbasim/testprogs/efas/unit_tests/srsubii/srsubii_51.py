from EFA_v2 import *
def srsubii_51():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7373257531943078089, 13, 1203]
    tran0.writeAction("movir X16 26195")
    tran0.writeAction("slorii X16 X16 12 298")
    tran0.writeAction("slorii X16 X16 12 2300")
    tran0.writeAction("slorii X16 X16 12 3852")
    tran0.writeAction("slorii X16 X16 12 2249")
    tran0.writeAction("srsubii X16 X17 13 1203")
    tran0.writeAction("yieldt")
    return efa
