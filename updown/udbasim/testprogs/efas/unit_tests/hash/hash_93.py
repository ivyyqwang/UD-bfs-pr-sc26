from EFA_v2 import *
def hash_93():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6717250110222062150, -5897553095185740935]
    tran0.writeAction("movir X16 41671")
    tran0.writeAction("slorii X16 X16 12 2185")
    tran0.writeAction("slorii X16 X16 12 3392")
    tran0.writeAction("slorii X16 X16 12 3114")
    tran0.writeAction("slorii X16 X16 12 3514")
    tran0.writeAction("movir X17 44583")
    tran0.writeAction("slorii X17 X17 12 2795")
    tran0.writeAction("slorii X17 X17 12 1245")
    tran0.writeAction("slorii X17 X17 12 1836")
    tran0.writeAction("slorii X17 X17 12 2937")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
