from EFA_v2 import *
def vmadd_i32_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2118125001, -191766896, 35653066, -1981093698, -1742717422, 694006447, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3913")
    tran0.writeAction("slorii X19 X19 12 478")
    tran0.writeAction("slorii X19 X19 8 144")
    tran0.writeAction("slorii X19 X19 12 2075")
    tran0.writeAction("slorii X19 X19 12 4090")
    tran0.writeAction("slorii X19 X19 8 55")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2206")
    tran0.writeAction("slorii X17 X17 12 2792")
    tran0.writeAction("slorii X17 X17 8 190")
    tran0.writeAction("slorii X17 X17 12 34")
    tran0.writeAction("slorii X17 X17 12 5")
    tran0.writeAction("slorii X17 X17 8 202")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 661")
    tran0.writeAction("slorii X18 X18 12 3506")
    tran0.writeAction("slorii X18 X18 8 175")
    tran0.writeAction("slorii X18 X18 12 2434")
    tran0.writeAction("slorii X18 X18 12 62")
    tran0.writeAction("slorii X18 X18 8 18")
    tran0.writeAction("vmadd.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
