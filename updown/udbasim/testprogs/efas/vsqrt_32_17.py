from EFA_v2 import *
def vsqrt_32_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3686119448, 2101780190, 2921708851, 2838043768, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2004")
    tran0.writeAction("slorii X19 X19 12 1694")
    tran0.writeAction("slorii X19 X19 8 222")
    tran0.writeAction("slorii X19 X19 12 3515")
    tran0.writeAction("slorii X19 X19 12 1464")
    tran0.writeAction("slorii X19 X19 8 24")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2706")
    tran0.writeAction("slorii X18 X18 12 2332")
    tran0.writeAction("slorii X18 X18 8 120")
    tran0.writeAction("slorii X18 X18 12 2786")
    tran0.writeAction("slorii X18 X18 12 1469")
    tran0.writeAction("slorii X18 X18 8 51")
    tran0.writeAction("vsqrt.32 X19 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
