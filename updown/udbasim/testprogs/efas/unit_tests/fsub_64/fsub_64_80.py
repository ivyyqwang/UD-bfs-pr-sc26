from EFA_v2 import *
def fsub_64_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4005140514560847840, 16632227925240186014]
    tran0.writeAction("movir X16 14229")
    tran0.writeAction("slorii X16 X16 12 481")
    tran0.writeAction("slorii X16 X16 12 1005")
    tran0.writeAction("slorii X16 X16 12 3786")
    tran0.writeAction("slorii X16 X16 12 4064")
    tran0.writeAction("movir X17 59089")
    tran0.writeAction("slorii X17 X17 12 2226")
    tran0.writeAction("slorii X17 X17 12 3387")
    tran0.writeAction("slorii X17 X17 12 1120")
    tran0.writeAction("slorii X17 X17 12 1182")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
