from EFA_v2 import *
def srsubii_40():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5189073405951810165, 6, 951]
    tran0.writeAction("movir X16 18435")
    tran0.writeAction("slorii X16 X16 12 1196")
    tran0.writeAction("slorii X16 X16 12 1299")
    tran0.writeAction("slorii X16 X16 12 753")
    tran0.writeAction("slorii X16 X16 12 2677")
    tran0.writeAction("srsubii X16 X17 6 951")
    tran0.writeAction("yieldt")
    return efa
