from EFA_v2 import *
def sli_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -30078")
    tran0.writeAction("slorii X16 X16 12 1697")
    tran0.writeAction("slorii X16 X16 12 1585")
    tran0.writeAction("slorii X16 X16 12 415")
    tran0.writeAction("slorii X16 X16 12 3387")
    tran0.writeAction("movir X17 31037")
    tran0.writeAction("slorii X17 X17 12 695")
    tran0.writeAction("slorii X17 X17 12 2196")
    tran0.writeAction("slorii X17 X17 12 3426")
    tran0.writeAction("slorii X17 X17 12 3601")
    tran0.writeAction("sli X16 X17 45")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
