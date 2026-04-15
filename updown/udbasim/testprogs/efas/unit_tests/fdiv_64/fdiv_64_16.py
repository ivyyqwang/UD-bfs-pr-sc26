from EFA_v2 import *
def fdiv_64_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [171233204467420046, 14441951393113394521]
    tran0.writeAction("movir X16 608")
    tran0.writeAction("slorii X16 X16 12 1403")
    tran0.writeAction("slorii X16 X16 12 310")
    tran0.writeAction("slorii X16 X16 12 132")
    tran0.writeAction("slorii X16 X16 12 2958")
    tran0.writeAction("movir X17 51308")
    tran0.writeAction("slorii X17 X17 12 484")
    tran0.writeAction("slorii X17 X17 12 1657")
    tran0.writeAction("slorii X17 X17 12 4020")
    tran0.writeAction("slorii X17 X17 12 3417")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
