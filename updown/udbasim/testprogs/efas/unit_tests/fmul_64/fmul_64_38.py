from EFA_v2 import *
def fmul_64_38():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12272526055697564055, 18229824355815199878]
    tran0.writeAction("movir X16 43600")
    tran0.writeAction("slorii X16 X16 12 3158")
    tran0.writeAction("slorii X16 X16 12 3278")
    tran0.writeAction("slorii X16 X16 12 2372")
    tran0.writeAction("slorii X16 X16 12 407")
    tran0.writeAction("movir X17 64765")
    tran0.writeAction("slorii X17 X17 12 1418")
    tran0.writeAction("slorii X17 X17 12 2678")
    tran0.writeAction("slorii X17 X17 12 529")
    tran0.writeAction("slorii X17 X17 12 1158")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
