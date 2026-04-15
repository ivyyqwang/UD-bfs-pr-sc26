from EFA_v2 import *
def div_25():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4976719173883089055, 3212892114230730049]
    tran0.writeAction("movir X16 17680")
    tran0.writeAction("slorii X16 X16 12 3515")
    tran0.writeAction("slorii X16 X16 12 2186")
    tran0.writeAction("slorii X16 X16 12 725")
    tran0.writeAction("slorii X16 X16 12 159")
    tran0.writeAction("movir X17 11414")
    tran0.writeAction("slorii X17 X17 12 1989")
    tran0.writeAction("slorii X17 X17 12 2802")
    tran0.writeAction("slorii X17 X17 12 1541")
    tran0.writeAction("slorii X17 X17 12 3393")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
