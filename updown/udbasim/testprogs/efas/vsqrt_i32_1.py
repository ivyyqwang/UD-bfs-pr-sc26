from EFA_v2 import *
def vsqrt_i32_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1701504962, -1001165754, -1454831956, 314173419, 0]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3141")
    tran0.writeAction("slorii X19 X19 12 876")
    tran0.writeAction("slorii X19 X19 8 70")
    tran0.writeAction("slorii X19 X19 12 1622")
    tran0.writeAction("slorii X19 X19 12 2791")
    tran0.writeAction("slorii X19 X19 8 194")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 299")
    tran0.writeAction("slorii X18 X18 12 2535")
    tran0.writeAction("slorii X18 X18 8 235")
    tran0.writeAction("slorii X18 X18 12 2708")
    tran0.writeAction("slorii X18 X18 12 2310")
    tran0.writeAction("slorii X18 X18 8 172")
    tran0.writeAction("vsqrt.i32 X19 X18 0 ")
    tran0.writeAction("yieldt")
    return efa
