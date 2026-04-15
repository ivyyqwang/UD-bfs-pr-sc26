from EFA_v2 import *
def vadd_b16_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2212, 52741, 63504, 65161, 22272, 31759, 14293, 28546, 27044, 11404, 24296, 46259, 4]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 4072")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 3969")
    tran0.writeAction("slorii X19 X19 4 0")
    tran0.writeAction("slorii X19 X19 12 3296")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("slorii X19 X19 12 138")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1784")
    tran0.writeAction("slorii X17 X17 4 2")
    tran0.writeAction("slorii X17 X17 12 893")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("slorii X17 X17 12 1984")
    tran0.writeAction("slorii X17 X17 4 15")
    tran0.writeAction("slorii X17 X17 12 1392")
    tran0.writeAction("slorii X17 X17 4 0")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2891")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 1518")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 712")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 1690")
    tran0.writeAction("slorii X18 X18 4 4")
    tran0.writeAction("vadd.b16 X19 X17 X18 4 ")
    tran0.writeAction("yieldt")
    return efa
