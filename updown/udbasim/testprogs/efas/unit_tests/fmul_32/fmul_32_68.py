from EFA_v2 import *
def fmul_32_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4256873116, 395931004]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 253")
    tran0.writeAction("slorii X16 X16 12 2987")
    tran0.writeAction("slorii X16 X16 12 2716")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 23")
    tran0.writeAction("slorii X17 X17 12 2454")
    tran0.writeAction("slorii X17 X17 12 3452")
    tran0.writeAction("fmul.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
