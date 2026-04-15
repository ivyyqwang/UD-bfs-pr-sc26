from EFA_v2 import *
def addi_81():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3063828622339418333, 29055]
    tran0.writeAction("movir X16 54651")
    tran0.writeAction("slorii X16 X16 12 385")
    tran0.writeAction("slorii X16 X16 12 2512")
    tran0.writeAction("slorii X16 X16 12 3213")
    tran0.writeAction("slorii X16 X16 12 1827")
    tran0.writeAction("addi X16 X17 29055")
    tran0.writeAction("yieldt")
    return efa
