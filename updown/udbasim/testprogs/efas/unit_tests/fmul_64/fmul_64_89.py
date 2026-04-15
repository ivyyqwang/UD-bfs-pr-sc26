from EFA_v2 import *
def fmul_64_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3823376113945472646, 16408388514893109791]
    tran0.writeAction("movir X16 13583")
    tran0.writeAction("slorii X16 X16 12 1477")
    tran0.writeAction("slorii X16 X16 12 394")
    tran0.writeAction("slorii X16 X16 12 1774")
    tran0.writeAction("slorii X16 X16 12 3718")
    tran0.writeAction("movir X17 58294")
    tran0.writeAction("slorii X17 X17 12 1254")
    tran0.writeAction("slorii X17 X17 12 2878")
    tran0.writeAction("slorii X17 X17 12 3289")
    tran0.writeAction("slorii X17 X17 12 2591")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
