from EFA_v2 import *
def divi_38():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4981374106906602424, 10416]
    tran0.writeAction("movir X16 17697")
    tran0.writeAction("slorii X16 X16 12 1621")
    tran0.writeAction("slorii X16 X16 12 2967")
    tran0.writeAction("slorii X16 X16 12 2034")
    tran0.writeAction("slorii X16 X16 12 3000")
    tran0.writeAction("divi X16 X17 10416")
    tran0.writeAction("yieldt")
    return efa
