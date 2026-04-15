from EFA_v2 import *
def vsub_b16_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5733, 10633, 18411, 24087, 58045, 15194, 35719, 55503, 50205, 20474, 36048, 29251, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1505")
    tran0.writeAction("slorii X19 X19 4 7")
    tran0.writeAction("slorii X19 X19 12 1150")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("slorii X19 X19 12 664")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 358")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3468")
    tran0.writeAction("slorii X17 X17 4 15")
    tran0.writeAction("slorii X17 X17 12 2232")
    tran0.writeAction("slorii X17 X17 4 7")
    tran0.writeAction("slorii X17 X17 12 949")
    tran0.writeAction("slorii X17 X17 4 10")
    tran0.writeAction("slorii X17 X17 12 3627")
    tran0.writeAction("slorii X17 X17 4 13")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1828")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 2253")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 1279")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 3137")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("vsub.b16 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
