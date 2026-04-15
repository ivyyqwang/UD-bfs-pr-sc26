from EFA_v2 import *
def subi_46():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8657810929571849456, -19147]
    tran0.writeAction("movir X16 34777")
    tran0.writeAction("slorii X16 X16 12 1133")
    tran0.writeAction("slorii X16 X16 12 1186")
    tran0.writeAction("slorii X16 X16 12 1537")
    tran0.writeAction("slorii X16 X16 12 2832")
    tran0.writeAction("subi X16 X17 -19147")
    tran0.writeAction("yieldt")
    return efa
