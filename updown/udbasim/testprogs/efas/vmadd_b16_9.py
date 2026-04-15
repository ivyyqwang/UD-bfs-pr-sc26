from EFA_v2 import *
def vmadd_b16_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10196, 52641, 47838, 22165, 1127, 27449, 12841, 9345, 10216, 38736, 3846, 39399, 13]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1385")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("slorii X19 X19 12 2989")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 3290")
    tran0.writeAction("slorii X19 X19 4 1")
    tran0.writeAction("slorii X19 X19 12 637")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 584")
    tran0.writeAction("slorii X17 X17 4 1")
    tran0.writeAction("slorii X17 X17 12 802")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("slorii X17 X17 12 1715")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("slorii X17 X17 12 70")
    tran0.writeAction("slorii X17 X17 4 7")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2462")
    tran0.writeAction("slorii X18 X18 4 7")
    tran0.writeAction("slorii X18 X18 12 240")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("slorii X18 X18 12 2421")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 638")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("vmadd.b16 X19 X17 X18 13 ")
    tran0.writeAction("yieldt")
    return efa
