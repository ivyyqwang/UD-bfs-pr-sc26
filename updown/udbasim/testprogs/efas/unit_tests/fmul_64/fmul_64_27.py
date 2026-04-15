from EFA_v2 import *
def fmul_64_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7462920259284060780, 7317276998046171291]
    tran0.writeAction("movir X16 26513")
    tran0.writeAction("slorii X16 X16 12 2534")
    tran0.writeAction("slorii X16 X16 12 3969")
    tran0.writeAction("slorii X16 X16 12 2836")
    tran0.writeAction("slorii X16 X16 12 2668")
    tran0.writeAction("movir X17 25996")
    tran0.writeAction("slorii X17 X17 12 778")
    tran0.writeAction("slorii X17 X17 12 2367")
    tran0.writeAction("slorii X17 X17 12 2780")
    tran0.writeAction("slorii X17 X17 12 155")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
