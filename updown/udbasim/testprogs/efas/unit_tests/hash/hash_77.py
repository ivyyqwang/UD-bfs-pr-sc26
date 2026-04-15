from EFA_v2 import *
def hash_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8904879257649018092, -5394634769936417847]
    tran0.writeAction("movir X16 33899")
    tran0.writeAction("slorii X16 X16 12 2103")
    tran0.writeAction("slorii X16 X16 12 3784")
    tran0.writeAction("slorii X16 X16 12 352")
    tran0.writeAction("slorii X16 X16 12 2836")
    tran0.writeAction("movir X17 46370")
    tran0.writeAction("slorii X17 X17 12 1668")
    tran0.writeAction("slorii X17 X17 12 572")
    tran0.writeAction("slorii X17 X17 12 3967")
    tran0.writeAction("slorii X17 X17 12 3017")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
