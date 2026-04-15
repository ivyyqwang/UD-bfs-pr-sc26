from EFA_v2 import *
def add_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5601293856331882016, -2609567214107211710]
    tran0.writeAction("movir X16 19899")
    tran0.writeAction("slorii X16 X16 12 3249")
    tran0.writeAction("slorii X16 X16 12 1501")
    tran0.writeAction("slorii X16 X16 12 981")
    tran0.writeAction("slorii X16 X16 12 3616")
    tran0.writeAction("movir X17 56264")
    tran0.writeAction("slorii X17 X17 12 3911")
    tran0.writeAction("slorii X17 X17 12 481")
    tran0.writeAction("slorii X17 X17 12 2596")
    tran0.writeAction("slorii X17 X17 12 2114")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
