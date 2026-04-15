from EFA_v2 import *
def fmul_64_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5355295312910359331, 3804466781963046589]
    tran0.writeAction("movir X16 19025")
    tran0.writeAction("slorii X16 X16 12 3403")
    tran0.writeAction("slorii X16 X16 12 1705")
    tran0.writeAction("slorii X16 X16 12 1377")
    tran0.writeAction("slorii X16 X16 12 2851")
    tran0.writeAction("movir X17 13516")
    tran0.writeAction("slorii X17 X17 12 742")
    tran0.writeAction("slorii X17 X17 12 410")
    tran0.writeAction("slorii X17 X17 12 2788")
    tran0.writeAction("slorii X17 X17 12 3773")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
