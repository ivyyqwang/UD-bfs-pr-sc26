from EFA_v2 import *
def fmul_64_92():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1037657510823892240, 2897307120429416049]
    tran0.writeAction("movir X16 3686")
    tran0.writeAction("slorii X16 X16 12 2048")
    tran0.writeAction("slorii X16 X16 12 547")
    tran0.writeAction("slorii X16 X16 12 713")
    tran0.writeAction("slorii X16 X16 12 1296")
    tran0.writeAction("movir X17 10293")
    tran0.writeAction("slorii X17 X17 12 1239")
    tran0.writeAction("slorii X17 X17 12 2486")
    tran0.writeAction("slorii X17 X17 12 1659")
    tran0.writeAction("slorii X17 X17 12 3697")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
