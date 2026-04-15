from EFA_v2 import *
def div_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6824319072587327156, 6424544522493659434]
    tran0.writeAction("movir X16 41291")
    tran0.writeAction("slorii X16 X16 12 607")
    tran0.writeAction("slorii X16 X16 12 1492")
    tran0.writeAction("slorii X16 X16 12 2085")
    tran0.writeAction("slorii X16 X16 12 2380")
    tran0.writeAction("movir X17 22824")
    tran0.writeAction("slorii X17 X17 12 2323")
    tran0.writeAction("slorii X17 X17 12 1114")
    tran0.writeAction("slorii X17 X17 12 3752")
    tran0.writeAction("slorii X17 X17 12 2346")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
