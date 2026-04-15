from EFA_v2 import *
def subi_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [256966978946712034, 11765]
    tran0.writeAction("movir X16 912")
    tran0.writeAction("slorii X16 X16 12 3809")
    tran0.writeAction("slorii X16 X16 12 2843")
    tran0.writeAction("slorii X16 X16 12 508")
    tran0.writeAction("slorii X16 X16 12 482")
    tran0.writeAction("subi X16 X17 11765")
    tran0.writeAction("yieldt")
    return efa
