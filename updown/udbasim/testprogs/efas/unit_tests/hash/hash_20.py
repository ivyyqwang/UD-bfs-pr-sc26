from EFA_v2 import *
def hash_20():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7400220257520369802, 6538450665304755067]
    tran0.writeAction("movir X16 39245")
    tran0.writeAction("slorii X16 X16 12 558")
    tran0.writeAction("slorii X16 X16 12 578")
    tran0.writeAction("slorii X16 X16 12 3475")
    tran0.writeAction("slorii X16 X16 12 3958")
    tran0.writeAction("movir X17 23229")
    tran0.writeAction("slorii X17 X17 12 995")
    tran0.writeAction("slorii X17 X17 12 3302")
    tran0.writeAction("slorii X17 X17 12 3712")
    tran0.writeAction("slorii X17 X17 12 2939")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
