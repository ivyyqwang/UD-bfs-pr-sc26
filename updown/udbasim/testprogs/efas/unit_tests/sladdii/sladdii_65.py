from EFA_v2 import *
def sladdii_65():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8322612394704823257, 6, 1678]
    tran0.writeAction("movir X16 29567")
    tran0.writeAction("slorii X16 X16 12 3518")
    tran0.writeAction("slorii X16 X16 12 189")
    tran0.writeAction("slorii X16 X16 12 2638")
    tran0.writeAction("slorii X16 X16 12 985")
    tran0.writeAction("sladdii X16 X17 6 1678")
    tran0.writeAction("yieldt")
    return efa
