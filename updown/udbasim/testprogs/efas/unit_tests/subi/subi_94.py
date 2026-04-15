from EFA_v2 import *
def subi_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2174350588072534567, -11217]
    tran0.writeAction("movir X16 7724")
    tran0.writeAction("slorii X16 X16 12 3461")
    tran0.writeAction("slorii X16 X16 12 1779")
    tran0.writeAction("slorii X16 X16 12 922")
    tran0.writeAction("slorii X16 X16 12 551")
    tran0.writeAction("subi X16 X17 -11217")
    tran0.writeAction("yieldt")
    return efa
