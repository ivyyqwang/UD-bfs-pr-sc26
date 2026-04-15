from EFA_v2 import *
def fsub_64_69():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10916219785165449018, 12866765785427338444]
    tran0.writeAction("movir X16 38782")
    tran0.writeAction("slorii X16 X16 12 832")
    tran0.writeAction("slorii X16 X16 12 3800")
    tran0.writeAction("slorii X16 X16 12 3594")
    tran0.writeAction("slorii X16 X16 12 1850")
    tran0.writeAction("movir X17 45711")
    tran0.writeAction("slorii X17 X17 12 3828")
    tran0.writeAction("slorii X17 X17 12 3984")
    tran0.writeAction("slorii X17 X17 12 2238")
    tran0.writeAction("slorii X17 X17 12 1228")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
