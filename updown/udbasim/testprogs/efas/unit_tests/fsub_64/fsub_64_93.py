from EFA_v2 import *
def fsub_64_93():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6650080952406094119, 7671107602363355689]
    tran0.writeAction("movir X16 23625")
    tran0.writeAction("slorii X16 X16 12 3414")
    tran0.writeAction("slorii X16 X16 12 1151")
    tran0.writeAction("slorii X16 X16 12 3099")
    tran0.writeAction("slorii X16 X16 12 295")
    tran0.writeAction("movir X17 27253")
    tran0.writeAction("slorii X17 X17 12 1019")
    tran0.writeAction("slorii X17 X17 12 2200")
    tran0.writeAction("slorii X17 X17 12 2729")
    tran0.writeAction("slorii X17 X17 12 553")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
