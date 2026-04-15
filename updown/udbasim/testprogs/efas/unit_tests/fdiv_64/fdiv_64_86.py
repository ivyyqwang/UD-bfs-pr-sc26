from EFA_v2 import *
def fdiv_64_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11699265515691705586, 14299488398110702209]
    tran0.writeAction("movir X16 41564")
    tran0.writeAction("slorii X16 X16 12 576")
    tran0.writeAction("slorii X16 X16 12 75")
    tran0.writeAction("slorii X16 X16 12 3200")
    tran0.writeAction("slorii X16 X16 12 1266")
    tran0.writeAction("movir X17 50801")
    tran0.writeAction("slorii X17 X17 12 4046")
    tran0.writeAction("slorii X17 X17 12 4007")
    tran0.writeAction("slorii X17 X17 12 851")
    tran0.writeAction("slorii X17 X17 12 2689")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
