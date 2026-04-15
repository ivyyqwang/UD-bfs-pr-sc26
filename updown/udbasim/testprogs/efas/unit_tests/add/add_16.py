from EFA_v2 import *
def add_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7879280635372138515, 6948216685857709924]
    tran0.writeAction("movir X16 27992")
    tran0.writeAction("slorii X16 X16 12 3391")
    tran0.writeAction("slorii X16 X16 12 3548")
    tran0.writeAction("slorii X16 X16 12 3975")
    tran0.writeAction("slorii X16 X16 12 19")
    tran0.writeAction("movir X17 24685")
    tran0.writeAction("slorii X17 X17 12 100")
    tran0.writeAction("slorii X17 X17 12 822")
    tran0.writeAction("slorii X17 X17 12 4057")
    tran0.writeAction("slorii X17 X17 12 3940")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
