from EFA_v2 import *
def sladdii_98():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [90579389604950844, 15, 1448]
    tran0.writeAction("movir X16 321")
    tran0.writeAction("slorii X16 X16 12 3287")
    tran0.writeAction("slorii X16 X16 12 2453")
    tran0.writeAction("slorii X16 X16 12 1535")
    tran0.writeAction("slorii X16 X16 12 828")
    tran0.writeAction("sladdii X16 X17 15 1448")
    tran0.writeAction("yieldt")
    return efa
