from EFA_v2 import *
def sar_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 9474")
    tran0.writeAction("slorii X16 X16 12 2417")
    tran0.writeAction("slorii X16 X16 12 2833")
    tran0.writeAction("slorii X16 X16 12 2305")
    tran0.writeAction("slorii X16 X16 12 3992")
    tran0.writeAction("movir X17 28492")
    tran0.writeAction("slorii X17 X17 12 2409")
    tran0.writeAction("slorii X17 X17 12 2684")
    tran0.writeAction("slorii X17 X17 12 842")
    tran0.writeAction("slorii X17 X17 12 2267")
    tran0.writeAction("movir X18 9233")
    tran0.writeAction("slorii X18 X18 12 2444")
    tran0.writeAction("slorii X18 X18 12 2701")
    tran0.writeAction("slorii X18 X18 12 895")
    tran0.writeAction("slorii X18 X18 12 2143")
    tran0.writeAction("sar X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
