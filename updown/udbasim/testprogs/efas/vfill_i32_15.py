from EFA_v2 import *
def vfill_i32_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [760806536, 168324685, 1597]
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 160")
    tran0.writeAction("slorii X18 X18 12 2158")
    tran0.writeAction("slorii X18 X18 8 77")
    tran0.writeAction("slorii X18 X18 12 725")
    tran0.writeAction("slorii X18 X18 12 2300")
    tran0.writeAction("slorii X18 X18 8 136")
    tran0.writeAction("vfill.i32 X18 1597 ")
    tran0.writeAction("yieldt")
    return efa
