from EFA_v2 import *
def mod_34():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2948821649503873181, -9043442754694110068]
    tran0.writeAction("movir X16 55059")
    tran0.writeAction("slorii X16 X16 12 2789")
    tran0.writeAction("slorii X16 X16 12 1363")
    tran0.writeAction("slorii X16 X16 12 1393")
    tran0.writeAction("slorii X16 X16 12 1891")
    tran0.writeAction("movir X17 33407")
    tran0.writeAction("slorii X17 X17 12 971")
    tran0.writeAction("slorii X17 X17 12 2707")
    tran0.writeAction("slorii X17 X17 12 3594")
    tran0.writeAction("slorii X17 X17 12 1164")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
