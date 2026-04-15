from EFA_v2 import *
def vsub_i32_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [593372278, 182727313, 357252211, 1152719596, -73708617, 1732177741, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 174")
    tran0.writeAction("slorii X19 X19 12 1074")
    tran0.writeAction("slorii X19 X19 8 145")
    tran0.writeAction("slorii X19 X19 12 565")
    tran0.writeAction("slorii X19 X19 12 3620")
    tran0.writeAction("slorii X19 X19 8 118")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1099")
    tran0.writeAction("slorii X17 X17 12 1306")
    tran0.writeAction("slorii X17 X17 8 236")
    tran0.writeAction("slorii X17 X17 12 340")
    tran0.writeAction("slorii X17 X17 12 2876")
    tran0.writeAction("slorii X17 X17 8 115")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1651")
    tran0.writeAction("slorii X18 X18 12 3823")
    tran0.writeAction("slorii X18 X18 8 77")
    tran0.writeAction("slorii X18 X18 12 4025")
    tran0.writeAction("slorii X18 X18 12 2891")
    tran0.writeAction("slorii X18 X18 8 183")
    tran0.writeAction("vsub.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
