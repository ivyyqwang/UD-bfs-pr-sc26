from EFA_v2 import *
def vgt_32_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4001886141, 1736874572, 1739117228, 3757281261, 303038882, 2368330628, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1656")
    tran0.writeAction("slorii X19 X19 12 1690")
    tran0.writeAction("slorii X19 X19 8 76")
    tran0.writeAction("slorii X19 X19 12 3816")
    tran0.writeAction("slorii X19 X19 12 2031")
    tran0.writeAction("slorii X19 X19 8 189")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3583")
    tran0.writeAction("slorii X17 X17 12 911")
    tran0.writeAction("slorii X17 X17 8 237")
    tran0.writeAction("slorii X17 X17 12 1658")
    tran0.writeAction("slorii X17 X17 12 2258")
    tran0.writeAction("slorii X17 X17 8 172")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2258")
    tran0.writeAction("slorii X18 X18 12 2523")
    tran0.writeAction("slorii X18 X18 8 132")
    tran0.writeAction("slorii X18 X18 12 289")
    tran0.writeAction("slorii X18 X18 12 1")
    tran0.writeAction("slorii X18 X18 8 162")
    tran0.writeAction("vgt.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
