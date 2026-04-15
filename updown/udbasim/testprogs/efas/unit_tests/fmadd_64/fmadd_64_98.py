from EFA_v2 import *
def fmadd_64_98():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13901661614010407347, 4651925582989505476, 13593984327130526818]
    tran0.writeAction("movir X16 49388")
    tran0.writeAction("slorii X16 X16 12 2553")
    tran0.writeAction("slorii X16 X16 12 1394")
    tran0.writeAction("slorii X16 X16 12 3169")
    tran0.writeAction("slorii X16 X16 12 2483")
    tran0.writeAction("movir X17 16526")
    tran0.writeAction("slorii X17 X17 12 3930")
    tran0.writeAction("slorii X17 X17 12 2999")
    tran0.writeAction("slorii X17 X17 12 2627")
    tran0.writeAction("slorii X17 X17 12 964")
    tran0.writeAction("movir X18 48295")
    tran0.writeAction("slorii X18 X18 12 2187")
    tran0.writeAction("slorii X18 X18 12 2228")
    tran0.writeAction("slorii X18 X18 12 3451")
    tran0.writeAction("slorii X18 X18 12 1122")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
