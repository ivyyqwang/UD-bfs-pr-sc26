from EFA_v2 import *
def addi_75():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6655129546202876967, 26081]
    tran0.writeAction("movir X16 41892")
    tran0.writeAction("slorii X16 X16 12 943")
    tran0.writeAction("slorii X16 X16 12 40")
    tran0.writeAction("slorii X16 X16 12 1519")
    tran0.writeAction("slorii X16 X16 12 985")
    tran0.writeAction("addi X16 X17 26081")
    tran0.writeAction("yieldt")
    return efa
