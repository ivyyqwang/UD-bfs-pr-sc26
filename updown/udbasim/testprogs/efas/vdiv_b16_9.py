from EFA_v2 import *
def vdiv_b16_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [45100, 1581, 23603, 54675, 29217, 37012, 54926, 50741, 4647, 8776, 23857, 6259, 13]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3417")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 1475")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 98")
    tran0.writeAction("slorii X19 X19 4 13")
    tran0.writeAction("slorii X19 X19 12 2818")
    tran0.writeAction("slorii X19 X19 4 12")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3171")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("slorii X17 X17 12 3432")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("slorii X17 X17 12 2313")
    tran0.writeAction("slorii X17 X17 4 4")
    tran0.writeAction("slorii X17 X17 12 1826")
    tran0.writeAction("slorii X17 X17 4 1")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 391")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 1491")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("slorii X18 X18 12 548")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 290")
    tran0.writeAction("slorii X18 X18 4 7")
    tran0.writeAction("vdiv.b16 X19 X17 X18 13 ")
    tran0.writeAction("yieldt")
    return efa
