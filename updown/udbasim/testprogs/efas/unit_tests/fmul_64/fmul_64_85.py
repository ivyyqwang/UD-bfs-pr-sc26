from EFA_v2 import *
def fmul_64_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15032665718904123279, 13177604904297626653]
    tran0.writeAction("movir X16 53406")
    tran0.writeAction("slorii X16 X16 12 3101")
    tran0.writeAction("slorii X16 X16 12 810")
    tran0.writeAction("slorii X16 X16 12 1934")
    tran0.writeAction("slorii X16 X16 12 3983")
    tran0.writeAction("movir X17 46816")
    tran0.writeAction("slorii X17 X17 12 1053")
    tran0.writeAction("slorii X17 X17 12 1967")
    tran0.writeAction("slorii X17 X17 12 431")
    tran0.writeAction("slorii X17 X17 12 3101")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
