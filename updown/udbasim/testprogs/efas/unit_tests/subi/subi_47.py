from EFA_v2 import *
def subi_47():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5442828152218837365, 27748]
    tran0.writeAction("movir X16 19336")
    tran0.writeAction("slorii X16 X16 12 3317")
    tran0.writeAction("slorii X16 X16 12 3578")
    tran0.writeAction("slorii X16 X16 12 2046")
    tran0.writeAction("slorii X16 X16 12 373")
    tran0.writeAction("subi X16 X17 27748")
    tran0.writeAction("yieldt")
    return efa
