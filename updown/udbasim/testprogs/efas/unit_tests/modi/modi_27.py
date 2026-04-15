from EFA_v2 import *
def modi_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7078538308389651679, -21790]
    tran0.writeAction("movir X16 40387")
    tran0.writeAction("slorii X16 X16 12 4014")
    tran0.writeAction("slorii X16 X16 12 2439")
    tran0.writeAction("slorii X16 X16 12 1803")
    tran0.writeAction("slorii X16 X16 12 2849")
    tran0.writeAction("modi X16 X17 -21790")
    tran0.writeAction("yieldt")
    return efa
