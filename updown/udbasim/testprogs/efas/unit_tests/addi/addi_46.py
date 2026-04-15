from EFA_v2 import *
def addi_46():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [435301438759788319, 32103]
    tran0.writeAction("movir X16 1546")
    tran0.writeAction("slorii X16 X16 12 2053")
    tran0.writeAction("slorii X16 X16 12 2603")
    tran0.writeAction("slorii X16 X16 12 2021")
    tran0.writeAction("slorii X16 X16 12 3871")
    tran0.writeAction("addi X16 X17 32103")
    tran0.writeAction("yieldt")
    return efa
