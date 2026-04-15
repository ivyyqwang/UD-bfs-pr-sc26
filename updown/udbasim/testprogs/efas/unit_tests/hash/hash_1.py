from EFA_v2 import *
def hash_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-171340404817823184, -5513672685811931838]
    tran0.writeAction("movir X16 64927")
    tran0.writeAction("slorii X16 X16 12 1132")
    tran0.writeAction("slorii X16 X16 12 3907")
    tran0.writeAction("slorii X16 X16 12 663")
    tran0.writeAction("slorii X16 X16 12 2608")
    tran0.writeAction("movir X17 45947")
    tran0.writeAction("slorii X17 X17 12 2046")
    tran0.writeAction("slorii X17 X17 12 1962")
    tran0.writeAction("slorii X17 X17 12 1662")
    tran0.writeAction("slorii X17 X17 12 1346")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
