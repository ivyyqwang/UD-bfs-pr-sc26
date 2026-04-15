from EFA_v2 import *
def div_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5174103742304935073, -1993917584646150988]
    tran0.writeAction("movir X16 18382")
    tran0.writeAction("slorii X16 X16 12 447")
    tran0.writeAction("slorii X16 X16 12 167")
    tran0.writeAction("slorii X16 X16 12 429")
    tran0.writeAction("slorii X16 X16 12 3233")
    tran0.writeAction("movir X17 58452")
    tran0.writeAction("slorii X17 X17 12 744")
    tran0.writeAction("slorii X17 X17 12 1375")
    tran0.writeAction("slorii X17 X17 12 3118")
    tran0.writeAction("slorii X17 X17 12 1204")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
