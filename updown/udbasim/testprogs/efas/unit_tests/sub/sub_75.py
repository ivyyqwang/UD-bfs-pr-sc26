from EFA_v2 import *
def sub_75():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4575017710802671986, -3228554545616579095]
    tran0.writeAction("movir X16 16253")
    tran0.writeAction("slorii X16 X16 12 2981")
    tran0.writeAction("slorii X16 X16 12 3669")
    tran0.writeAction("slorii X16 X16 12 2105")
    tran0.writeAction("slorii X16 X16 12 2418")
    tran0.writeAction("movir X17 54065")
    tran0.writeAction("slorii X17 X17 12 3563")
    tran0.writeAction("slorii X17 X17 12 3858")
    tran0.writeAction("slorii X17 X17 12 2257")
    tran0.writeAction("slorii X17 X17 12 1513")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
