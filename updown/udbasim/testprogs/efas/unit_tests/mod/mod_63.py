from EFA_v2 import *
def mod_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7411018782065366141, -9187525021719340407]
    tran0.writeAction("movir X16 26329")
    tran0.writeAction("slorii X16 X16 12 933")
    tran0.writeAction("slorii X16 X16 12 296")
    tran0.writeAction("slorii X16 X16 12 3089")
    tran0.writeAction("slorii X16 X16 12 1149")
    tran0.writeAction("movir X17 32895")
    tran0.writeAction("slorii X17 X17 12 1450")
    tran0.writeAction("slorii X17 X17 12 2971")
    tran0.writeAction("slorii X17 X17 12 1661")
    tran0.writeAction("slorii X17 X17 12 2697")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
