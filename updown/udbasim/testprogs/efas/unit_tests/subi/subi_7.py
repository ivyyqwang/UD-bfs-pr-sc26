from EFA_v2 import *
def subi_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3744597350101852957, 1569]
    tran0.writeAction("movir X16 13303")
    tran0.writeAction("slorii X16 X16 12 1975")
    tran0.writeAction("slorii X16 X16 12 831")
    tran0.writeAction("slorii X16 X16 12 2826")
    tran0.writeAction("slorii X16 X16 12 797")
    tran0.writeAction("subi X16 X17 1569")
    tran0.writeAction("yieldt")
    return efa
