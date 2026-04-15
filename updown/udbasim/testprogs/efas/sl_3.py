from EFA_v2 import *
def sl_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -2779")
    tran0.writeAction("slorii X16 X16 12 1417")
    tran0.writeAction("slorii X16 X16 12 3797")
    tran0.writeAction("slorii X16 X16 12 1614")
    tran0.writeAction("slorii X16 X16 12 1896")
    tran0.writeAction("movir X17 20383")
    tran0.writeAction("slorii X17 X17 12 1271")
    tran0.writeAction("slorii X17 X17 12 3118")
    tran0.writeAction("slorii X17 X17 12 2789")
    tran0.writeAction("slorii X17 X17 12 1255")
    tran0.writeAction("movir X18 3651")
    tran0.writeAction("slorii X18 X18 12 467")
    tran0.writeAction("slorii X18 X18 12 536")
    tran0.writeAction("slorii X18 X18 12 2684")
    tran0.writeAction("slorii X18 X18 12 165")
    tran0.writeAction("sl X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
