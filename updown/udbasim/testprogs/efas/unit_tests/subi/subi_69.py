from EFA_v2 import *
def subi_69():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [447332022823420748, -23790]
    tran0.writeAction("movir X16 1589")
    tran0.writeAction("slorii X16 X16 12 993")
    tran0.writeAction("slorii X16 X16 12 2765")
    tran0.writeAction("slorii X16 X16 12 192")
    tran0.writeAction("slorii X16 X16 12 844")
    tran0.writeAction("subi X16 X17 -23790")
    tran0.writeAction("yieldt")
    return efa
