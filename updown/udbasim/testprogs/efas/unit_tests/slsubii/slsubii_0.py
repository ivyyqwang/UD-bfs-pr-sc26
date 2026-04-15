from EFA_v2 import *
def slsubii_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6523860706098466232, 8, 757]
    tran0.writeAction("movir X16 23177")
    tran0.writeAction("slorii X16 X16 12 1675")
    tran0.writeAction("slorii X16 X16 12 3919")
    tran0.writeAction("slorii X16 X16 12 524")
    tran0.writeAction("slorii X16 X16 12 3512")
    tran0.writeAction("slsubii X16 X17 8 757")
    tran0.writeAction("yieldt")
    return efa
