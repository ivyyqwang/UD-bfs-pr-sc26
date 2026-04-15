from EFA_v2 import *
def subi_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7276520257019414651, 21950]
    tran0.writeAction("movir X16 39684")
    tran0.writeAction("slorii X16 X16 12 2486")
    tran0.writeAction("slorii X16 X16 12 255")
    tran0.writeAction("slorii X16 X16 12 1735")
    tran0.writeAction("slorii X16 X16 12 1925")
    tran0.writeAction("subi X16 X17 21950")
    tran0.writeAction("yieldt")
    return efa
