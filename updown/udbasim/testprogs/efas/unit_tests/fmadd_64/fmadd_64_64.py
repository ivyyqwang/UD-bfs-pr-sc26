from EFA_v2 import *
def fmadd_64_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4036181066884311142, 73617443032099472, 263339888927606790]
    tran0.writeAction("movir X16 14339")
    tran0.writeAction("slorii X16 X16 12 1620")
    tran0.writeAction("slorii X16 X16 12 2996")
    tran0.writeAction("slorii X16 X16 12 3262")
    tran0.writeAction("slorii X16 X16 12 2150")
    tran0.writeAction("movir X17 261")
    tran0.writeAction("slorii X17 X17 12 2218")
    tran0.writeAction("slorii X17 X17 12 3237")
    tran0.writeAction("slorii X17 X17 12 822")
    tran0.writeAction("slorii X17 X17 12 2704")
    tran0.writeAction("movir X18 935")
    tran0.writeAction("slorii X18 X18 12 2339")
    tran0.writeAction("slorii X18 X18 12 3030")
    tran0.writeAction("slorii X18 X18 12 2952")
    tran0.writeAction("slorii X18 X18 12 2054")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
