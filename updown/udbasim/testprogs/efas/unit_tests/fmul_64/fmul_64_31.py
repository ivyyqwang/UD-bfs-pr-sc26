from EFA_v2 import *
def fmul_64_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13652816890612246466, 12054318721287890834]
    tran0.writeAction("movir X16 48504")
    tran0.writeAction("slorii X16 X16 12 2250")
    tran0.writeAction("slorii X16 X16 12 84")
    tran0.writeAction("slorii X16 X16 12 1622")
    tran0.writeAction("slorii X16 X16 12 1986")
    tran0.writeAction("movir X17 42825")
    tran0.writeAction("slorii X17 X17 12 2224")
    tran0.writeAction("slorii X17 X17 12 687")
    tran0.writeAction("slorii X17 X17 12 2890")
    tran0.writeAction("slorii X17 X17 12 1938")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
