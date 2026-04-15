from EFA_v2 import *
def subi_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2736018091210321708, 27198]
    tran0.writeAction("movir X16 55815")
    tran0.writeAction("slorii X16 X16 12 2912")
    tran0.writeAction("slorii X16 X16 12 2758")
    tran0.writeAction("slorii X16 X16 12 1501")
    tran0.writeAction("slorii X16 X16 12 212")
    tran0.writeAction("subi X16 X17 27198")
    tran0.writeAction("yieldt")
    return efa
