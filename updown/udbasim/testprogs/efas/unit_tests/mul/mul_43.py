from EFA_v2 import *
def mul_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8454366663380779049, -5359407128550630356]
    tran0.writeAction("movir X16 35500")
    tran0.writeAction("slorii X16 X16 12 229")
    tran0.writeAction("slorii X16 X16 12 20")
    tran0.writeAction("slorii X16 X16 12 1163")
    tran0.writeAction("slorii X16 X16 12 4055")
    tran0.writeAction("movir X17 46495")
    tran0.writeAction("slorii X17 X17 12 2297")
    tran0.writeAction("slorii X17 X17 12 3240")
    tran0.writeAction("slorii X17 X17 12 177")
    tran0.writeAction("slorii X17 X17 12 3116")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
