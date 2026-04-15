from EFA_v2 import *
def andi_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 486")
    tran0.writeAction("slorii X16 X16 12 1038")
    tran0.writeAction("slorii X16 X16 12 1536")
    tran0.writeAction("slorii X16 X16 12 1760")
    tran0.writeAction("slorii X16 X16 12 877")
    tran0.writeAction("movir X17 30119")
    tran0.writeAction("slorii X17 X17 12 3469")
    tran0.writeAction("slorii X17 X17 12 3055")
    tran0.writeAction("slorii X17 X17 12 1815")
    tran0.writeAction("slorii X17 X17 12 3554")
    tran0.writeAction("andi X16 X17 -14485")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
