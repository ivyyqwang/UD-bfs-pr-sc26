from EFA_v2 import *
def divi_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-9003884132953409209, -376]
    tran0.writeAction("movir X16 33547")
    tran0.writeAction("slorii X16 X16 12 3185")
    tran0.writeAction("slorii X16 X16 12 1520")
    tran0.writeAction("slorii X16 X16 12 2195")
    tran0.writeAction("slorii X16 X16 12 2375")
    tran0.writeAction("divi X16 X17 -376")
    tran0.writeAction("yieldt")
    return efa
