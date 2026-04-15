from EFA_v2 import *
def mul_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6896436548416574069, -5748329060877991401]
    tran0.writeAction("movir X16 41034")
    tran0.writeAction("slorii X16 X16 12 3831")
    tran0.writeAction("slorii X16 X16 12 3971")
    tran0.writeAction("slorii X16 X16 12 2494")
    tran0.writeAction("slorii X16 X16 12 3467")
    tran0.writeAction("movir X17 45113")
    tran0.writeAction("slorii X17 X17 12 3410")
    tran0.writeAction("slorii X17 X17 12 3282")
    tran0.writeAction("slorii X17 X17 12 1280")
    tran0.writeAction("slorii X17 X17 12 535")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
