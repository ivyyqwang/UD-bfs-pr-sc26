from EFA_v2 import *
def vmul_32_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2606524172, 3387929833, 1359895648, 4154888606, 2573891078, 2796297616, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3230")
    tran0.writeAction("slorii X19 X19 12 4020")
    tran0.writeAction("slorii X19 X19 8 233")
    tran0.writeAction("slorii X19 X19 12 2485")
    tran0.writeAction("slorii X19 X19 12 3175")
    tran0.writeAction("slorii X19 X19 8 12")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3962")
    tran0.writeAction("slorii X17 X17 12 1681")
    tran0.writeAction("slorii X17 X17 8 158")
    tran0.writeAction("slorii X17 X17 12 1296")
    tran0.writeAction("slorii X17 X17 12 3676")
    tran0.writeAction("slorii X17 X17 8 96")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2666")
    tran0.writeAction("slorii X18 X18 12 3101")
    tran0.writeAction("slorii X18 X18 8 144")
    tran0.writeAction("slorii X18 X18 12 2454")
    tran0.writeAction("slorii X18 X18 12 2678")
    tran0.writeAction("slorii X18 X18 8 6")
    tran0.writeAction("vmul.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
