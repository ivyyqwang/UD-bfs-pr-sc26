from EFA_v2 import *
def srsubii_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4727899963265685566, 2, 2047]
    tran0.writeAction("movir X16 48739")
    tran0.writeAction("slorii X16 X16 12 512")
    tran0.writeAction("slorii X16 X16 12 2155")
    tran0.writeAction("slorii X16 X16 12 3958")
    tran0.writeAction("slorii X16 X16 12 1986")
    tran0.writeAction("srsubii X16 X17 2 2047")
    tran0.writeAction("yieldt")
    return efa
