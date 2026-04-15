from EFA_v2 import *
def srori_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 24371")
    tran0.writeAction("slorii X16 X16 12 3023")
    tran0.writeAction("slorii X16 X16 12 635")
    tran0.writeAction("slorii X16 X16 12 1134")
    tran0.writeAction("slorii X16 X16 12 1305")
    tran0.writeAction("movir X17 -12911")
    tran0.writeAction("slorii X17 X17 12 3947")
    tran0.writeAction("slorii X17 X17 12 2239")
    tran0.writeAction("slorii X17 X17 12 2003")
    tran0.writeAction("slorii X17 X17 12 3585")
    tran0.writeAction("srori X16 X17 31")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
