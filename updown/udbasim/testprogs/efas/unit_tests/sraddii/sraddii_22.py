from EFA_v2 import *
def sraddii_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1385135741712768750, 6, 1568]
    tran0.writeAction("movir X16 60615")
    tran0.writeAction("slorii X16 X16 12 38")
    tran0.writeAction("slorii X16 X16 12 437")
    tran0.writeAction("slorii X16 X16 12 2102")
    tran0.writeAction("slorii X16 X16 12 274")
    tran0.writeAction("sraddii X16 X17 6 1568")
    tran0.writeAction("yieldt")
    return efa
