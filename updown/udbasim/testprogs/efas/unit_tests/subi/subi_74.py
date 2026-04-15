from EFA_v2 import *
def subi_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8672840187491620753, 19544]
    tran0.writeAction("movir X16 30812")
    tran0.writeAction("slorii X16 X16 12 483")
    tran0.writeAction("slorii X16 X16 12 809")
    tran0.writeAction("slorii X16 X16 12 697")
    tran0.writeAction("slorii X16 X16 12 1937")
    tran0.writeAction("subi X16 X17 19544")
    tran0.writeAction("yieldt")
    return efa
