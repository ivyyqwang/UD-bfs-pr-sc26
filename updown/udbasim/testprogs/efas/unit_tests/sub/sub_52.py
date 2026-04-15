from EFA_v2 import *
def sub_52():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3425820889235792998, -1221287505407440641]
    tran0.writeAction("movir X16 53365")
    tran0.writeAction("slorii X16 X16 12 160")
    tran0.writeAction("slorii X16 X16 12 3408")
    tran0.writeAction("slorii X16 X16 12 4045")
    tran0.writeAction("slorii X16 X16 12 2970")
    tran0.writeAction("movir X17 61197")
    tran0.writeAction("slorii X17 X17 12 471")
    tran0.writeAction("slorii X17 X17 12 3079")
    tran0.writeAction("slorii X17 X17 12 2320")
    tran0.writeAction("slorii X17 X17 12 2303")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
