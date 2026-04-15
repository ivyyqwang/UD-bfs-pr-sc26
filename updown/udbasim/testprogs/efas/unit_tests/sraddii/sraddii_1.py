from EFA_v2 import *
def sraddii_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6093243530476171824, 2, 1071]
    tran0.writeAction("movir X16 43888")
    tran0.writeAction("slorii X16 X16 12 1844")
    tran0.writeAction("slorii X16 X16 12 2780")
    tran0.writeAction("slorii X16 X16 12 84")
    tran0.writeAction("slorii X16 X16 12 3536")
    tran0.writeAction("sraddii X16 X17 2 1071")
    tran0.writeAction("yieldt")
    return efa
