from EFA_v2 import *
def srsubii_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2068121793925202643, 9, 1532]
    tran0.writeAction("movir X16 58188")
    tran0.writeAction("slorii X16 X16 12 2274")
    tran0.writeAction("slorii X16 X16 12 3984")
    tran0.writeAction("slorii X16 X16 12 3459")
    tran0.writeAction("slorii X16 X16 12 3373")
    tran0.writeAction("srsubii X16 X17 9 1532")
    tran0.writeAction("yieldt")
    return efa
