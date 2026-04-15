from EFA_v2 import *
def mul_50():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3251284720174763090, -3706077700545957586]
    tran0.writeAction("movir X16 11550")
    tran0.writeAction("slorii X16 X16 12 3619")
    tran0.writeAction("slorii X16 X16 12 2585")
    tran0.writeAction("slorii X16 X16 12 2752")
    tran0.writeAction("slorii X16 X16 12 3154")
    tran0.writeAction("movir X17 52369")
    tran0.writeAction("slorii X17 X17 12 1503")
    tran0.writeAction("slorii X17 X17 12 1932")
    tran0.writeAction("slorii X17 X17 12 3939")
    tran0.writeAction("slorii X17 X17 12 302")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
