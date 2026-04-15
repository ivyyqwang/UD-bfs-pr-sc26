from EFA_v2 import *
def vadd_i32_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-525302330, 1447886293, 1087045551, -1296768456, 151777863, 1708140637, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1380")
    tran0.writeAction("slorii X19 X19 12 3325")
    tran0.writeAction("slorii X19 X19 8 213")
    tran0.writeAction("slorii X19 X19 12 3595")
    tran0.writeAction("slorii X19 X19 12 133")
    tran0.writeAction("slorii X19 X19 8 198")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2859")
    tran0.writeAction("slorii X17 X17 12 1250")
    tran0.writeAction("slorii X17 X17 8 56")
    tran0.writeAction("slorii X17 X17 12 1036")
    tran0.writeAction("slorii X17 X17 12 2815")
    tran0.writeAction("slorii X17 X17 8 175")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1629")
    tran0.writeAction("slorii X18 X18 12 40")
    tran0.writeAction("slorii X18 X18 8 93")
    tran0.writeAction("slorii X18 X18 12 144")
    tran0.writeAction("slorii X18 X18 12 3058")
    tran0.writeAction("slorii X18 X18 8 71")
    tran0.writeAction("vadd.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
