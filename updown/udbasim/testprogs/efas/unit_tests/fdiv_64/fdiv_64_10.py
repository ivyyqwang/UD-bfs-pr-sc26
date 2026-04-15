from EFA_v2 import *
def fdiv_64_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6553852561038251246, 447644674324337534]
    tran0.writeAction("movir X16 23283")
    tran0.writeAction("slorii X16 X16 12 3938")
    tran0.writeAction("slorii X16 X16 12 3634")
    tran0.writeAction("slorii X16 X16 12 3969")
    tran0.writeAction("slorii X16 X16 12 1262")
    tran0.writeAction("movir X17 1590")
    tran0.writeAction("slorii X17 X17 12 1447")
    tran0.writeAction("slorii X17 X17 12 1446")
    tran0.writeAction("slorii X17 X17 12 2857")
    tran0.writeAction("slorii X17 X17 12 894")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
