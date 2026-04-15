from EFA_v2 import *
def fsub_64_21():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3900391059273472585, 13312436557683121150]
    tran0.writeAction("movir X16 13856")
    tran0.writeAction("slorii X16 X16 12 3984")
    tran0.writeAction("slorii X16 X16 12 213")
    tran0.writeAction("slorii X16 X16 12 429")
    tran0.writeAction("slorii X16 X16 12 2633")
    tran0.writeAction("movir X17 47295")
    tran0.writeAction("slorii X17 X17 12 1128")
    tran0.writeAction("slorii X17 X17 12 1107")
    tran0.writeAction("slorii X17 X17 12 2565")
    tran0.writeAction("slorii X17 X17 12 3070")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
