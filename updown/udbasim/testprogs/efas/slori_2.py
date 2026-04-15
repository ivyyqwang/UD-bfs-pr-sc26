from EFA_v2 import *
def slori_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -25580")
    tran0.writeAction("slorii X16 X16 12 3124")
    tran0.writeAction("slorii X16 X16 12 1694")
    tran0.writeAction("slorii X16 X16 12 1726")
    tran0.writeAction("slorii X16 X16 12 2848")
    tran0.writeAction("movir X17 -17992")
    tran0.writeAction("slorii X17 X17 12 696")
    tran0.writeAction("slorii X17 X17 12 2164")
    tran0.writeAction("slorii X17 X17 12 2746")
    tran0.writeAction("slorii X17 X17 12 225")
    tran0.writeAction("slori X16 X17 39")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
