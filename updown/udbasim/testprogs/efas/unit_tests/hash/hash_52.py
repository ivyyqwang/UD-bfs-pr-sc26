from EFA_v2 import *
def hash_52():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1770233871229847484, 5433377676255928303]
    tran0.writeAction("movir X16 59246")
    tran0.writeAction("slorii X16 X16 12 3546")
    tran0.writeAction("slorii X16 X16 12 3159")
    tran0.writeAction("slorii X16 X16 12 4015")
    tran0.writeAction("slorii X16 X16 12 2116")
    tran0.writeAction("movir X17 19303")
    tran0.writeAction("slorii X17 X17 12 963")
    tran0.writeAction("slorii X17 X17 12 1427")
    tran0.writeAction("slorii X17 X17 12 3161")
    tran0.writeAction("slorii X17 X17 12 4079")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
