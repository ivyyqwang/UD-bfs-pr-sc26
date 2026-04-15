from EFA_v2 import *
def fsub_64_34():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13923776215147610517, 1187971718868407469]
    tran0.writeAction("movir X16 49467")
    tran0.writeAction("slorii X16 X16 12 779")
    tran0.writeAction("slorii X16 X16 12 579")
    tran0.writeAction("slorii X16 X16 12 3712")
    tran0.writeAction("slorii X16 X16 12 405")
    tran0.writeAction("movir X17 4220")
    tran0.writeAction("slorii X17 X17 12 2143")
    tran0.writeAction("slorii X17 X17 12 3058")
    tran0.writeAction("slorii X17 X17 12 1481")
    tran0.writeAction("slorii X17 X17 12 1197")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
