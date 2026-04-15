from EFA_v2 import *
def mod_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2069898251786563383, 7446087647115564922]
    tran0.writeAction("movir X16 58182")
    tran0.writeAction("slorii X16 X16 12 1000")
    tran0.writeAction("slorii X16 X16 12 445")
    tran0.writeAction("slorii X16 X16 12 245")
    tran0.writeAction("slorii X16 X16 12 201")
    tran0.writeAction("movir X17 26453")
    tran0.writeAction("slorii X17 X17 12 3348")
    tran0.writeAction("slorii X17 X17 12 916")
    tran0.writeAction("slorii X17 X17 12 3061")
    tran0.writeAction("slorii X17 X17 12 1914")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
