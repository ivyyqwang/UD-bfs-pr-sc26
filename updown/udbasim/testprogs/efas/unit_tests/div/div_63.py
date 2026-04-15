from EFA_v2 import *
def div_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1260177224802509691, 550557196393068580]
    tran0.writeAction("movir X16 61058")
    tran0.writeAction("slorii X16 X16 12 3895")
    tran0.writeAction("slorii X16 X16 12 3489")
    tran0.writeAction("slorii X16 X16 12 2493")
    tran0.writeAction("slorii X16 X16 12 3205")
    tran0.writeAction("movir X17 1955")
    tran0.writeAction("slorii X17 X17 12 3981")
    tran0.writeAction("slorii X17 X17 12 2663")
    tran0.writeAction("slorii X17 X17 12 2227")
    tran0.writeAction("slorii X17 X17 12 2084")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
