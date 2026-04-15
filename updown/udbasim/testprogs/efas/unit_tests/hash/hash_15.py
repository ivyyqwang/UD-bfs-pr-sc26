from EFA_v2 import *
def hash_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6474854899676859979, 7929734120298129774]
    tran0.writeAction("movir X16 42532")
    tran0.writeAction("slorii X16 X16 12 2844")
    tran0.writeAction("slorii X16 X16 12 1572")
    tran0.writeAction("slorii X16 X16 12 2307")
    tran0.writeAction("slorii X16 X16 12 437")
    tran0.writeAction("movir X17 28172")
    tran0.writeAction("slorii X17 X17 12 306")
    tran0.writeAction("slorii X17 X17 12 2875")
    tran0.writeAction("slorii X17 X17 12 2722")
    tran0.writeAction("slorii X17 X17 12 2414")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
