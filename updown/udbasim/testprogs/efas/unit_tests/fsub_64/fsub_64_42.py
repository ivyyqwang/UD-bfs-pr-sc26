from EFA_v2 import *
def fsub_64_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3816708087517366789, 18272272339225790467]
    tran0.writeAction("movir X16 13559")
    tran0.writeAction("slorii X16 X16 12 2748")
    tran0.writeAction("slorii X16 X16 12 2215")
    tran0.writeAction("slorii X16 X16 12 3412")
    tran0.writeAction("slorii X16 X16 12 2565")
    tran0.writeAction("movir X17 64916")
    tran0.writeAction("slorii X17 X17 12 622")
    tran0.writeAction("slorii X17 X17 12 450")
    tran0.writeAction("slorii X17 X17 12 3068")
    tran0.writeAction("slorii X17 X17 12 2051")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
