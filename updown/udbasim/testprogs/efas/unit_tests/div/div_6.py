from EFA_v2 import *
def div_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5314733430774742033, -7156050442991396135]
    tran0.writeAction("movir X16 18881")
    tran0.writeAction("slorii X16 X16 12 2974")
    tran0.writeAction("slorii X16 X16 12 1417")
    tran0.writeAction("slorii X16 X16 12 907")
    tran0.writeAction("slorii X16 X16 12 3089")
    tran0.writeAction("movir X17 40112")
    tran0.writeAction("slorii X17 X17 12 2464")
    tran0.writeAction("slorii X17 X17 12 2390")
    tran0.writeAction("slorii X17 X17 12 2953")
    tran0.writeAction("slorii X17 X17 12 2777")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
