from EFA_v2 import *
def add_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5835171851845112426, 2257810871654322878]
    tran0.writeAction("movir X16 44805")
    tran0.writeAction("slorii X16 X16 12 1249")
    tran0.writeAction("slorii X16 X16 12 3559")
    tran0.writeAction("slorii X16 X16 12 1694")
    tran0.writeAction("slorii X16 X16 12 3478")
    tran0.writeAction("movir X17 8021")
    tran0.writeAction("slorii X17 X17 12 1456")
    tran0.writeAction("slorii X17 X17 12 1662")
    tran0.writeAction("slorii X17 X17 12 3977")
    tran0.writeAction("slorii X17 X17 12 702")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
