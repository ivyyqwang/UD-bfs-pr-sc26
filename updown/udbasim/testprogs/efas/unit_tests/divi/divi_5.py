from EFA_v2 import *
def divi_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [693394447945651438, -24930]
    tran0.writeAction("movir X16 2463")
    tran0.writeAction("slorii X16 X16 12 1769")
    tran0.writeAction("slorii X16 X16 12 927")
    tran0.writeAction("slorii X16 X16 12 117")
    tran0.writeAction("slorii X16 X16 12 1262")
    tran0.writeAction("divi X16 X17 -24930")
    tran0.writeAction("yieldt")
    return efa
