from EFA_v2 import *
def divi_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5391636374667565658, 9412]
    tran0.writeAction("movir X16 46381")
    tran0.writeAction("slorii X16 X16 12 244")
    tran0.writeAction("slorii X16 X16 12 2185")
    tran0.writeAction("slorii X16 X16 12 3542")
    tran0.writeAction("slorii X16 X16 12 1446")
    tran0.writeAction("divi X16 X17 9412")
    tran0.writeAction("yieldt")
    return efa
