from EFA_v2 import *
def fmul_32_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2182694424, 1333940391]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 130")
    tran0.writeAction("slorii X16 X16 12 404")
    tran0.writeAction("slorii X16 X16 12 1560")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 79")
    tran0.writeAction("slorii X17 X17 12 2085")
    tran0.writeAction("slorii X17 X17 12 167")
    tran0.writeAction("fmul.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
