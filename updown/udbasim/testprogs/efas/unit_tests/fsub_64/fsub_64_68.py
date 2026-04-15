from EFA_v2 import *
def fsub_64_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18260107148548648110, 4184081176041951779]
    tran0.writeAction("movir X16 64872")
    tran0.writeAction("slorii X16 X16 12 3819")
    tran0.writeAction("slorii X16 X16 12 1173")
    tran0.writeAction("slorii X16 X16 12 3330")
    tran0.writeAction("slorii X16 X16 12 3246")
    tran0.writeAction("movir X17 14864")
    tran0.writeAction("slorii X17 X17 12 3450")
    tran0.writeAction("slorii X17 X17 12 2385")
    tran0.writeAction("slorii X17 X17 12 1553")
    tran0.writeAction("slorii X17 X17 12 547")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
