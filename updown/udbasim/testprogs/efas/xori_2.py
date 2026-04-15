from EFA_v2 import *
def xori_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 14413")
    tran0.writeAction("slorii X16 X16 12 1022")
    tran0.writeAction("slorii X16 X16 12 3578")
    tran0.writeAction("slorii X16 X16 12 940")
    tran0.writeAction("slorii X16 X16 12 2080")
    tran0.writeAction("movir X17 9009")
    tran0.writeAction("slorii X17 X17 12 2344")
    tran0.writeAction("slorii X17 X17 12 342")
    tran0.writeAction("slorii X17 X17 12 2659")
    tran0.writeAction("slorii X17 X17 12 3026")
    tran0.writeAction("xori X16 X17 -28147")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
