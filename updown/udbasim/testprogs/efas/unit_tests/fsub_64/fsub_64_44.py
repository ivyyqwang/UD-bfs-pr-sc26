from EFA_v2 import *
def fsub_64_44():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15962953947029051626, 16608965918966761220]
    tran0.writeAction("movir X16 56711")
    tran0.writeAction("slorii X16 X16 12 3296")
    tran0.writeAction("slorii X16 X16 12 2586")
    tran0.writeAction("slorii X16 X16 12 2401")
    tran0.writeAction("slorii X16 X16 12 2282")
    tran0.writeAction("movir X17 59006")
    tran0.writeAction("slorii X17 X17 12 3688")
    tran0.writeAction("slorii X17 X17 12 342")
    tran0.writeAction("slorii X17 X17 12 2388")
    tran0.writeAction("slorii X17 X17 12 1796")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
