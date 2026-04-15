from EFA_v2 import *
def subi_29():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7458048121559124302, -27201]
    tran0.writeAction("movir X16 26496")
    tran0.writeAction("slorii X16 X16 12 1268")
    tran0.writeAction("slorii X16 X16 12 139")
    tran0.writeAction("slorii X16 X16 12 1232")
    tran0.writeAction("slorii X16 X16 12 2382")
    tran0.writeAction("subi X16 X17 -27201")
    tran0.writeAction("yieldt")
    return efa
