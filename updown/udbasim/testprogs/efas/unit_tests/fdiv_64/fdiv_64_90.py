from EFA_v2 import *
def fdiv_64_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7064777202356960721, 15574108941087246983]
    tran0.writeAction("movir X16 25099")
    tran0.writeAction("slorii X16 X16 12 534")
    tran0.writeAction("slorii X16 X16 12 3915")
    tran0.writeAction("slorii X16 X16 12 3131")
    tran0.writeAction("slorii X16 X16 12 3537")
    tran0.writeAction("movir X17 55330")
    tran0.writeAction("slorii X17 X17 12 1433")
    tran0.writeAction("slorii X17 X17 12 278")
    tran0.writeAction("slorii X17 X17 12 3032")
    tran0.writeAction("slorii X17 X17 12 2695")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
