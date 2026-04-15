from EFA_v2 import *
def fdiv_64_26():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4344232656204017333, 14589815037320352869]
    tran0.writeAction("movir X16 15433")
    tran0.writeAction("slorii X16 X16 12 3337")
    tran0.writeAction("slorii X16 X16 12 1414")
    tran0.writeAction("slorii X16 X16 12 2834")
    tran0.writeAction("slorii X16 X16 12 3765")
    tran0.writeAction("movir X17 51833")
    tran0.writeAction("slorii X17 X17 12 1783")
    tran0.writeAction("slorii X17 X17 12 2542")
    tran0.writeAction("slorii X17 X17 12 541")
    tran0.writeAction("slorii X17 X17 12 1125")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
