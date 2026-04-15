from EFA_v2 import *
def srsubii_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1840202229848606990, 0, 826]
    tran0.writeAction("movir X16 6537")
    tran0.writeAction("slorii X16 X16 12 2914")
    tran0.writeAction("slorii X16 X16 12 3489")
    tran0.writeAction("slorii X16 X16 12 32")
    tran0.writeAction("slorii X16 X16 12 2318")
    tran0.writeAction("srsubii X16 X17 0 826")
    tran0.writeAction("yieldt")
    return efa
