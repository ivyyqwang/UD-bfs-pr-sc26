from EFA_v2 import *
def fmul_64_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12568180930107722893, 16213291359371602058]
    tran0.writeAction("movir X16 44651")
    tran0.writeAction("slorii X16 X16 12 607")
    tran0.writeAction("slorii X16 X16 12 1923")
    tran0.writeAction("slorii X16 X16 12 3724")
    tran0.writeAction("slorii X16 X16 12 3213")
    tran0.writeAction("movir X17 57601")
    tran0.writeAction("slorii X17 X17 12 745")
    tran0.writeAction("slorii X17 X17 12 1779")
    tran0.writeAction("slorii X17 X17 12 1042")
    tran0.writeAction("slorii X17 X17 12 2186")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
