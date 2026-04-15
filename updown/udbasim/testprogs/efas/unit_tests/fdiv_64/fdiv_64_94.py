from EFA_v2 import *
def fdiv_64_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [879109617242710270, 17630188754645831852]
    tran0.writeAction("movir X16 3123")
    tran0.writeAction("slorii X16 X16 12 920")
    tran0.writeAction("slorii X16 X16 12 2566")
    tran0.writeAction("slorii X16 X16 12 1562")
    tran0.writeAction("slorii X16 X16 12 254")
    tran0.writeAction("movir X17 62635")
    tran0.writeAction("slorii X17 X17 12 52")
    tran0.writeAction("slorii X17 X17 12 891")
    tran0.writeAction("slorii X17 X17 12 3077")
    tran0.writeAction("slorii X17 X17 12 172")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
