from EFA_v2 import *
def fsub_64_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3663438711739948425, 5831752376769489833]
    tran0.writeAction("movir X16 13015")
    tran0.writeAction("slorii X16 X16 12 609")
    tran0.writeAction("slorii X16 X16 12 2365")
    tran0.writeAction("slorii X16 X16 12 2761")
    tran0.writeAction("slorii X16 X16 12 3465")
    tran0.writeAction("movir X17 20718")
    tran0.writeAction("slorii X17 X17 12 2238")
    tran0.writeAction("slorii X17 X17 12 899")
    tran0.writeAction("slorii X17 X17 12 1578")
    tran0.writeAction("slorii X17 X17 12 2985")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
