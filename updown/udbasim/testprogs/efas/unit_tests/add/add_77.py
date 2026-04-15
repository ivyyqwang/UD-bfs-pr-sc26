from EFA_v2 import *
def add_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2624395122323241014, -6998627675095484670]
    tran0.writeAction("movir X16 9323")
    tran0.writeAction("slorii X16 X16 12 2967")
    tran0.writeAction("slorii X16 X16 12 1416")
    tran0.writeAction("slorii X16 X16 12 1411")
    tran0.writeAction("slorii X16 X16 12 2102")
    tran0.writeAction("movir X17 40671")
    tran0.writeAction("slorii X17 X17 12 3603")
    tran0.writeAction("slorii X17 X17 12 1462")
    tran0.writeAction("slorii X17 X17 12 2931")
    tran0.writeAction("slorii X17 X17 12 1794")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
