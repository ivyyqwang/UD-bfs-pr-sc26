from EFA_v2 import *
def mul_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5644862517926903219, -8986876454586342781]
    tran0.writeAction("movir X16 20054")
    tran0.writeAction("slorii X16 X16 12 2376")
    tran0.writeAction("slorii X16 X16 12 3426")
    tran0.writeAction("slorii X16 X16 12 3891")
    tran0.writeAction("slorii X16 X16 12 3507")
    tran0.writeAction("movir X17 33608")
    tran0.writeAction("slorii X17 X17 12 823")
    tran0.writeAction("slorii X17 X17 12 2724")
    tran0.writeAction("slorii X17 X17 12 242")
    tran0.writeAction("slorii X17 X17 12 643")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
