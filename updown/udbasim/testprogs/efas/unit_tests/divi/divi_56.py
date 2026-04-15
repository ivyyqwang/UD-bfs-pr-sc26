from EFA_v2 import *
def divi_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7885217899833640522, 18938]
    tran0.writeAction("movir X16 37522")
    tran0.writeAction("slorii X16 X16 12 321")
    tran0.writeAction("slorii X16 X16 12 2311")
    tran0.writeAction("slorii X16 X16 12 3539")
    tran0.writeAction("slorii X16 X16 12 2486")
    tran0.writeAction("divi X16 X17 18938")
    tran0.writeAction("yieldt")
    return efa
