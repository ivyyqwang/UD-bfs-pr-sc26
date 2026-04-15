from EFA_v2 import *
def add_54():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7915997108971572630, -5653393136930916238]
    tran0.writeAction("movir X16 37412")
    tran0.writeAction("slorii X16 X16 12 2985")
    tran0.writeAction("slorii X16 X16 12 500")
    tran0.writeAction("slorii X16 X16 12 2991")
    tran0.writeAction("slorii X16 X16 12 618")
    tran0.writeAction("movir X17 45451")
    tran0.writeAction("slorii X17 X17 12 462")
    tran0.writeAction("slorii X17 X17 12 1305")
    tran0.writeAction("slorii X17 X17 12 2463")
    tran0.writeAction("slorii X17 X17 12 2162")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
