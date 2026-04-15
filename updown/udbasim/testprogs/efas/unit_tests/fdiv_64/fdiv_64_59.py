from EFA_v2 import *
def fdiv_64_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7822083802703081360, 5608638598110691885]
    tran0.writeAction("movir X16 27789")
    tran0.writeAction("slorii X16 X16 12 2556")
    tran0.writeAction("slorii X16 X16 12 1663")
    tran0.writeAction("slorii X16 X16 12 1858")
    tran0.writeAction("slorii X16 X16 12 3984")
    tran0.writeAction("movir X17 19925")
    tran0.writeAction("slorii X17 X17 12 3633")
    tran0.writeAction("slorii X17 X17 12 1745")
    tran0.writeAction("slorii X17 X17 12 3820")
    tran0.writeAction("slorii X17 X17 12 557")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
