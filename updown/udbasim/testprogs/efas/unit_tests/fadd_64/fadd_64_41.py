from EFA_v2 import *
def fadd_64_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8762055704223029419, 4868766638339488944]
    tran0.writeAction("movir X16 31129")
    tran0.writeAction("slorii X16 X16 12 307")
    tran0.writeAction("slorii X16 X16 12 3416")
    tran0.writeAction("slorii X16 X16 12 1633")
    tran0.writeAction("slorii X16 X16 12 2219")
    tran0.writeAction("movir X17 17297")
    tran0.writeAction("slorii X17 X17 12 1367")
    tran0.writeAction("slorii X17 X17 12 1588")
    tran0.writeAction("slorii X17 X17 12 2039")
    tran0.writeAction("slorii X17 X17 12 3248")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
