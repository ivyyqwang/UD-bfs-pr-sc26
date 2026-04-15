from EFA_v2 import *
def fcnvt_64_b16_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5707792027727807148]
    tran0.writeAction("movir X16 20278")
    tran0.writeAction("slorii X16 X16 12 617")
    tran0.writeAction("slorii X16 X16 12 2984")
    tran0.writeAction("slorii X16 X16 12 2140")
    tran0.writeAction("slorii X16 X16 12 684")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
