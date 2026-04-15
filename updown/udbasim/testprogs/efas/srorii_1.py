from EFA_v2 import *
def srorii_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 4131")
    tran0.writeAction("slorii X16 X16 12 2826")
    tran0.writeAction("slorii X16 X16 12 1963")
    tran0.writeAction("slorii X16 X16 12 2008")
    tran0.writeAction("slorii X16 X16 12 3542")
    tran0.writeAction("movir X17 23605")
    tran0.writeAction("slorii X17 X17 12 1719")
    tran0.writeAction("slorii X17 X17 12 2532")
    tran0.writeAction("slorii X17 X17 12 2884")
    tran0.writeAction("slorii X17 X17 12 4086")
    tran0.writeAction("srorii X16 X17 0 2302")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
