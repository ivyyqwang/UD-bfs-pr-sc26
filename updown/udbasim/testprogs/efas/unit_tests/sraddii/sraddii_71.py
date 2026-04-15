from EFA_v2 import *
def sraddii_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4306108582726278974, 9, 1912]
    tran0.writeAction("movir X16 50237")
    tran0.writeAction("slorii X16 X16 12 2576")
    tran0.writeAction("slorii X16 X16 12 3850")
    tran0.writeAction("slorii X16 X16 12 1390")
    tran0.writeAction("slorii X16 X16 12 194")
    tran0.writeAction("sraddii X16 X17 9 1912")
    tran0.writeAction("yieldt")
    return efa
