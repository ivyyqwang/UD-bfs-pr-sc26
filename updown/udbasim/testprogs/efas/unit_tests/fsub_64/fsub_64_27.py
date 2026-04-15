from EFA_v2 import *
def fsub_64_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13612050735816381776, 11619624317732125090]
    tran0.writeAction("movir X16 48359")
    tran0.writeAction("slorii X16 X16 12 2944")
    tran0.writeAction("slorii X16 X16 12 1604")
    tran0.writeAction("slorii X16 X16 12 3809")
    tran0.writeAction("slorii X16 X16 12 1360")
    tran0.writeAction("movir X17 41281")
    tran0.writeAction("slorii X17 X17 12 812")
    tran0.writeAction("slorii X17 X17 12 233")
    tran0.writeAction("slorii X17 X17 12 3743")
    tran0.writeAction("slorii X17 X17 12 2466")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
