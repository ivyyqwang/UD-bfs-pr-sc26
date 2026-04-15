from EFA_v2 import *
def sraddii_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2088892065990595934, 5, 1934]
    tran0.writeAction("movir X16 58114")
    tran0.writeAction("slorii X16 X16 12 3131")
    tran0.writeAction("slorii X16 X16 12 3008")
    tran0.writeAction("slorii X16 X16 12 2042")
    tran0.writeAction("slorii X16 X16 12 2722")
    tran0.writeAction("sraddii X16 X17 5 1934")
    tran0.writeAction("yieldt")
    return efa
