from EFA_v2 import *
def divi_82():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-470426540022464331, 24066]
    tran0.writeAction("movir X16 63864")
    tran0.writeAction("slorii X16 X16 12 2904")
    tran0.writeAction("slorii X16 X16 12 3557")
    tran0.writeAction("slorii X16 X16 12 184")
    tran0.writeAction("slorii X16 X16 12 181")
    tran0.writeAction("divi X16 X17 24066")
    tran0.writeAction("yieldt")
    return efa
