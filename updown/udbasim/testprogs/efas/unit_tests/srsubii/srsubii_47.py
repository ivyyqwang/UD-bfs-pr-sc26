from EFA_v2 import *
def srsubii_47():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7079864878462489070, 5, 126]
    tran0.writeAction("movir X16 25152")
    tran0.writeAction("slorii X16 X16 12 3001")
    tran0.writeAction("slorii X16 X16 12 2210")
    tran0.writeAction("slorii X16 X16 12 2133")
    tran0.writeAction("slorii X16 X16 12 494")
    tran0.writeAction("srsubii X16 X17 5 126")
    tran0.writeAction("yieldt")
    return efa
