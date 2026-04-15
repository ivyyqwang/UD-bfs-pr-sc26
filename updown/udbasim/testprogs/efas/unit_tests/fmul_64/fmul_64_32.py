from EFA_v2 import *
def fmul_64_32():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15361036603215039148, 9849695497005934164]
    tran0.writeAction("movir X16 54573")
    tran0.writeAction("slorii X16 X16 12 1494")
    tran0.writeAction("slorii X16 X16 12 1924")
    tran0.writeAction("slorii X16 X16 12 1660")
    tran0.writeAction("slorii X16 X16 12 2732")
    tran0.writeAction("movir X17 34993")
    tran0.writeAction("slorii X17 X17 12 605")
    tran0.writeAction("slorii X17 X17 12 3676")
    tran0.writeAction("slorii X17 X17 12 3290")
    tran0.writeAction("slorii X17 X17 12 1620")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
