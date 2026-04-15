from EFA_v2 import *
def mod_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7549758794441573690, -2600104125138831191]
    tran0.writeAction("movir X16 26822")
    tran0.writeAction("slorii X16 X16 12 537")
    tran0.writeAction("slorii X16 X16 12 3978")
    tran0.writeAction("slorii X16 X16 12 2340")
    tran0.writeAction("slorii X16 X16 12 1338")
    tran0.writeAction("movir X17 56298")
    tran0.writeAction("slorii X17 X17 12 2353")
    tran0.writeAction("slorii X17 X17 12 762")
    tran0.writeAction("slorii X17 X17 12 295")
    tran0.writeAction("slorii X17 X17 12 2217")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
