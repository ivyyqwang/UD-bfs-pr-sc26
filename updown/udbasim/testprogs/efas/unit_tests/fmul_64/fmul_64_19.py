from EFA_v2 import *
def fmul_64_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3973377072788005781, 1832144700979329693]
    tran0.writeAction("movir X16 14116")
    tran0.writeAction("slorii X16 X16 12 1110")
    tran0.writeAction("slorii X16 X16 12 1366")
    tran0.writeAction("slorii X16 X16 12 862")
    tran0.writeAction("slorii X16 X16 12 917")
    tran0.writeAction("movir X17 6509")
    tran0.writeAction("slorii X17 X17 12 350")
    tran0.writeAction("slorii X17 X17 12 1534")
    tran0.writeAction("slorii X17 X17 12 4043")
    tran0.writeAction("slorii X17 X17 12 2717")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
