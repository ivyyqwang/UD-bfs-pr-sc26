from EFA_v2 import *
def subi_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5881726267468070356, 30934]
    tran0.writeAction("movir X16 20896")
    tran0.writeAction("slorii X16 X16 12 366")
    tran0.writeAction("slorii X16 X16 12 166")
    tran0.writeAction("slorii X16 X16 12 2123")
    tran0.writeAction("slorii X16 X16 12 3540")
    tran0.writeAction("subi X16 X17 30934")
    tran0.writeAction("yieldt")
    return efa
