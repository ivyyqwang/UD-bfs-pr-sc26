from EFA_v2 import *
def fmul_32_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3101322553, 1540949017]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 184")
    tran0.writeAction("slorii X16 X16 12 3494")
    tran0.writeAction("slorii X16 X16 12 3385")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 91")
    tran0.writeAction("slorii X17 X17 12 3472")
    tran0.writeAction("slorii X17 X17 12 1049")
    tran0.writeAction("fmul.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
