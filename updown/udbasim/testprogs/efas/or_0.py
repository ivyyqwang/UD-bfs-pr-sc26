from EFA_v2 import *
def or_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 19399")
    tran0.writeAction("slorii X16 X16 12 2965")
    tran0.writeAction("slorii X16 X16 12 3291")
    tran0.writeAction("slorii X16 X16 12 3152")
    tran0.writeAction("slorii X16 X16 12 2062")
    tran0.writeAction("movir X17 9110")
    tran0.writeAction("slorii X17 X17 12 2045")
    tran0.writeAction("slorii X17 X17 12 2800")
    tran0.writeAction("slorii X17 X17 12 1257")
    tran0.writeAction("slorii X17 X17 12 3417")
    tran0.writeAction("movir X18 29948")
    tran0.writeAction("slorii X18 X18 12 3077")
    tran0.writeAction("slorii X18 X18 12 2376")
    tran0.writeAction("slorii X18 X18 12 2157")
    tran0.writeAction("slorii X18 X18 12 2547")
    tran0.writeAction("or X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
