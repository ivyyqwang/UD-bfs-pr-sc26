from EFA_v2 import *
def fdiv_64_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3947042356584193439, 14748569184663875701]
    tran0.writeAction("movir X16 14022")
    tran0.writeAction("slorii X16 X16 12 2913")
    tran0.writeAction("slorii X16 X16 12 3177")
    tran0.writeAction("slorii X16 X16 12 2545")
    tran0.writeAction("slorii X16 X16 12 3487")
    tran0.writeAction("movir X17 52397")
    tran0.writeAction("slorii X17 X17 12 1816")
    tran0.writeAction("slorii X17 X17 12 2109")
    tran0.writeAction("slorii X17 X17 12 667")
    tran0.writeAction("slorii X17 X17 12 117")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
