from EFA_v2 import *
def hash_92():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [305515743097137558, 187922095831912247]
    tran0.writeAction("movir X16 1085")
    tran0.writeAction("slorii X16 X16 12 1679")
    tran0.writeAction("slorii X16 X16 12 796")
    tran0.writeAction("slorii X16 X16 12 2434")
    tran0.writeAction("slorii X16 X16 12 2454")
    tran0.writeAction("movir X17 667")
    tran0.writeAction("slorii X17 X17 12 2594")
    tran0.writeAction("slorii X17 X17 12 1671")
    tran0.writeAction("slorii X17 X17 12 2080")
    tran0.writeAction("slorii X17 X17 12 3895")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
