from EFA_v2 import *
def mod_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6635547485619002489, 4621183047701629564]
    tran0.writeAction("movir X16 23574")
    tran0.writeAction("slorii X16 X16 12 820")
    tran0.writeAction("slorii X16 X16 12 2066")
    tran0.writeAction("slorii X16 X16 12 2281")
    tran0.writeAction("slorii X16 X16 12 3193")
    tran0.writeAction("movir X17 16417")
    tran0.writeAction("slorii X17 X17 12 3031")
    tran0.writeAction("slorii X17 X17 12 3952")
    tran0.writeAction("slorii X17 X17 12 1280")
    tran0.writeAction("slorii X17 X17 12 2684")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
