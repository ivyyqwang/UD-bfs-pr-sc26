from EFA_v2 import *
def mod_70():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2001092745308905434, -9037270769451803424]
    tran0.writeAction("movir X16 58426")
    tran0.writeAction("slorii X16 X16 12 2828")
    tran0.writeAction("slorii X16 X16 12 25")
    tran0.writeAction("slorii X16 X16 12 1030")
    tran0.writeAction("slorii X16 X16 12 38")
    tran0.writeAction("movir X17 33429")
    tran0.writeAction("slorii X17 X17 12 673")
    tran0.writeAction("slorii X17 X17 12 3551")
    tran0.writeAction("slorii X17 X17 12 3293")
    tran0.writeAction("slorii X17 X17 12 3296")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
