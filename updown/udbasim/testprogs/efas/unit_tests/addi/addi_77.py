from EFA_v2 import *
def addi_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4473862460954224008, -24797]
    tran0.writeAction("movir X16 15894")
    tran0.writeAction("slorii X16 X16 12 1443")
    tran0.writeAction("slorii X16 X16 12 1127")
    tran0.writeAction("slorii X16 X16 12 538")
    tran0.writeAction("slorii X16 X16 12 1416")
    tran0.writeAction("addi X16 X17 -24797")
    tran0.writeAction("yieldt")
    return efa
