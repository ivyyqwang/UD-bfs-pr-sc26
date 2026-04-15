from EFA_v2 import *
def vadd_i32_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [366758751, -322302572, -1756489471, 102377765, 186298393, 10563056, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3788")
    tran0.writeAction("slorii X19 X19 12 2573")
    tran0.writeAction("slorii X19 X19 8 148")
    tran0.writeAction("slorii X19 X19 12 349")
    tran0.writeAction("slorii X19 X19 12 3147")
    tran0.writeAction("slorii X19 X19 8 95")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 97")
    tran0.writeAction("slorii X17 X17 12 2601")
    tran0.writeAction("slorii X17 X17 8 37")
    tran0.writeAction("slorii X17 X17 12 2420")
    tran0.writeAction("slorii X17 X17 12 3609")
    tran0.writeAction("slorii X17 X17 8 1")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 10")
    tran0.writeAction("slorii X18 X18 12 301")
    tran0.writeAction("slorii X18 X18 8 240")
    tran0.writeAction("slorii X18 X18 12 177")
    tran0.writeAction("slorii X18 X18 12 2736")
    tran0.writeAction("slorii X18 X18 8 25")
    tran0.writeAction("vadd.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
