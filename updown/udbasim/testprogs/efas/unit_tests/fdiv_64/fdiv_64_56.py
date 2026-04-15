from EFA_v2 import *
def fdiv_64_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8048812457533098734, 9071142712967999690]
    tran0.writeAction("movir X16 28595")
    tran0.writeAction("slorii X16 X16 12 516")
    tran0.writeAction("slorii X16 X16 12 2338")
    tran0.writeAction("slorii X16 X16 12 4092")
    tran0.writeAction("slorii X16 X16 12 2798")
    tran0.writeAction("movir X17 32227")
    tran0.writeAction("slorii X17 X17 12 707")
    tran0.writeAction("slorii X17 X17 12 3209")
    tran0.writeAction("slorii X17 X17 12 1355")
    tran0.writeAction("slorii X17 X17 12 202")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
