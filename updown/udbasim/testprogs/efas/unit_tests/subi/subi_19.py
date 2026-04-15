from EFA_v2 import *
def subi_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6427320990788934433, -17871]
    tran0.writeAction("movir X16 42701")
    tran0.writeAction("slorii X16 X16 12 2329")
    tran0.writeAction("slorii X16 X16 12 3262")
    tran0.writeAction("slorii X16 X16 12 2514")
    tran0.writeAction("slorii X16 X16 12 1247")
    tran0.writeAction("subi X16 X17 -17871")
    tran0.writeAction("yieldt")
    return efa
