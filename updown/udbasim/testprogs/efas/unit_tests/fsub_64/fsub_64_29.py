from EFA_v2 import *
def fsub_64_29():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5925055437961148561, 2833926533072309879]
    tran0.writeAction("movir X16 21050")
    tran0.writeAction("slorii X16 X16 12 104")
    tran0.writeAction("slorii X16 X16 12 1870")
    tran0.writeAction("slorii X16 X16 12 699")
    tran0.writeAction("slorii X16 X16 12 2193")
    tran0.writeAction("movir X17 10068")
    tran0.writeAction("slorii X17 X17 12 530")
    tran0.writeAction("slorii X17 X17 12 2755")
    tran0.writeAction("slorii X17 X17 12 1348")
    tran0.writeAction("slorii X17 X17 12 3703")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
