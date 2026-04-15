from EFA_v2 import *
def divi_92():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6569202780135309351, 28001]
    tran0.writeAction("movir X16 42197")
    tran0.writeAction("slorii X16 X16 12 2062")
    tran0.writeAction("slorii X16 X16 12 104")
    tran0.writeAction("slorii X16 X16 12 2155")
    tran0.writeAction("slorii X16 X16 12 4057")
    tran0.writeAction("divi X16 X17 28001")
    tran0.writeAction("yieldt")
    return efa
