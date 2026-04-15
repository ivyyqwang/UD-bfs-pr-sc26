from EFA_v2 import *
def vmul_b16_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [58712, 2205, 40708, 10331, 6539, 41838, 46182, 58, 45194, 41721, 22322, 23344, 15]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 645")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("slorii X19 X19 12 2544")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("slorii X19 X19 12 137")
    tran0.writeAction("slorii X19 X19 4 13")
    tran0.writeAction("slorii X19 X19 12 3669")
    tran0.writeAction("slorii X19 X19 4 8")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3")
    tran0.writeAction("slorii X17 X17 4 10")
    tran0.writeAction("slorii X17 X17 12 2886")
    tran0.writeAction("slorii X17 X17 4 6")
    tran0.writeAction("slorii X17 X17 12 2614")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("slorii X17 X17 12 408")
    tran0.writeAction("slorii X17 X17 4 11")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1459")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 1395")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("slorii X18 X18 12 2607")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 2824")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("vmul.b16 X19 X17 X18 15 ")
    tran0.writeAction("yieldt")
    return efa
