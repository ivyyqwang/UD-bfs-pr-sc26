from EFA_v2 import *
def xori_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -24555")
    tran0.writeAction("slorii X16 X16 12 487")
    tran0.writeAction("slorii X16 X16 12 3363")
    tran0.writeAction("slorii X16 X16 12 3516")
    tran0.writeAction("slorii X16 X16 12 3723")
    tran0.writeAction("movir X17 31648")
    tran0.writeAction("slorii X17 X17 12 2245")
    tran0.writeAction("slorii X17 X17 12 4012")
    tran0.writeAction("slorii X17 X17 12 1155")
    tran0.writeAction("slorii X17 X17 12 1475")
    tran0.writeAction("xori X16 X17 -18648")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
