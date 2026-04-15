from EFA_v2 import *
def fmul_64_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2321388681156143950, 5528196095334573037]
    tran0.writeAction("movir X16 8247")
    tran0.writeAction("slorii X16 X16 12 939")
    tran0.writeAction("slorii X16 X16 12 1229")
    tran0.writeAction("slorii X16 X16 12 3786")
    tran0.writeAction("slorii X16 X16 12 2894")
    tran0.writeAction("movir X17 19640")
    tran0.writeAction("slorii X17 X17 12 400")
    tran0.writeAction("slorii X17 X17 12 3871")
    tran0.writeAction("slorii X17 X17 12 486")
    tran0.writeAction("slorii X17 X17 12 1005")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
