from EFA_v2 import *
def fmul_64_83():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17735598522142882442, 14101905426179202403]
    tran0.writeAction("movir X16 63009")
    tran0.writeAction("slorii X16 X16 12 2062")
    tran0.writeAction("slorii X16 X16 12 895")
    tran0.writeAction("slorii X16 X16 12 1103")
    tran0.writeAction("slorii X16 X16 12 2698")
    tran0.writeAction("movir X17 50100")
    tran0.writeAction("slorii X17 X17 12 132")
    tran0.writeAction("slorii X17 X17 12 1311")
    tran0.writeAction("slorii X17 X17 12 2313")
    tran0.writeAction("slorii X17 X17 12 3427")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
