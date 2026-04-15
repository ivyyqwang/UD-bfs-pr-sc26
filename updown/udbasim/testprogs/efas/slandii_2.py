from EFA_v2 import *
def slandii_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -21386")
    tran0.writeAction("slorii X16 X16 12 920")
    tran0.writeAction("slorii X16 X16 12 3157")
    tran0.writeAction("slorii X16 X16 12 2621")
    tran0.writeAction("slorii X16 X16 12 775")
    tran0.writeAction("movir X17 -3948")
    tran0.writeAction("slorii X17 X17 12 2065")
    tran0.writeAction("slorii X17 X17 12 3355")
    tran0.writeAction("slorii X17 X17 12 2300")
    tran0.writeAction("slorii X17 X17 12 393")
    tran0.writeAction("slandii X16 X17 12 3136")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
