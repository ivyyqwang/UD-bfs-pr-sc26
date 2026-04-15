from EFA_v2 import *
def fdiv_64_20():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9074556195073114351, 6228287437337309708]
    tran0.writeAction("movir X16 32239")
    tran0.writeAction("slorii X16 X16 12 1228")
    tran0.writeAction("slorii X16 X16 12 1989")
    tran0.writeAction("slorii X16 X16 12 2676")
    tran0.writeAction("slorii X16 X16 12 239")
    tran0.writeAction("movir X17 22127")
    tran0.writeAction("slorii X17 X17 12 1318")
    tran0.writeAction("slorii X17 X17 12 3301")
    tran0.writeAction("slorii X17 X17 12 2123")
    tran0.writeAction("slorii X17 X17 12 524")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
