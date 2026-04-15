from EFA_v2 import *
def fdiv_64_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12716396669490642996, 7449916936907183300]
    tran0.writeAction("movir X16 45177")
    tran0.writeAction("slorii X16 X16 12 2934")
    tran0.writeAction("slorii X16 X16 12 1411")
    tran0.writeAction("slorii X16 X16 12 3892")
    tran0.writeAction("slorii X16 X16 12 52")
    tran0.writeAction("movir X17 26467")
    tran0.writeAction("slorii X17 X17 12 1727")
    tran0.writeAction("slorii X17 X17 12 2966")
    tran0.writeAction("slorii X17 X17 12 2125")
    tran0.writeAction("slorii X17 X17 12 1220")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
