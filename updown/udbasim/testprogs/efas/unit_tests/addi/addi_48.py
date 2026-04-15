from EFA_v2 import *
def addi_48():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7997657877446015267, 22977]
    tran0.writeAction("movir X16 37122")
    tran0.writeAction("slorii X16 X16 12 2504")
    tran0.writeAction("slorii X16 X16 12 2219")
    tran0.writeAction("slorii X16 X16 12 2972")
    tran0.writeAction("slorii X16 X16 12 1757")
    tran0.writeAction("addi X16 X17 22977")
    tran0.writeAction("yieldt")
    return efa
