from EFA_v2 import *
def vgt_i32_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1984102827, 1516120268, -708698194, 1602173052, 2103372878, 322571013, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1445")
    tran0.writeAction("slorii X19 X19 12 3624")
    tran0.writeAction("slorii X19 X19 8 204")
    tran0.writeAction("slorii X19 X19 12 1892")
    tran0.writeAction("slorii X19 X19 12 769")
    tran0.writeAction("slorii X19 X19 8 171")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1527")
    tran0.writeAction("slorii X17 X17 12 3896")
    tran0.writeAction("slorii X17 X17 8 124")
    tran0.writeAction("slorii X17 X17 12 3420")
    tran0.writeAction("slorii X17 X17 12 543")
    tran0.writeAction("slorii X17 X17 8 174")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 307")
    tran0.writeAction("slorii X18 X18 12 2571")
    tran0.writeAction("slorii X18 X18 8 5")
    tran0.writeAction("slorii X18 X18 12 2005")
    tran0.writeAction("slorii X18 X18 12 3820")
    tran0.writeAction("slorii X18 X18 8 78")
    tran0.writeAction("vgt.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
