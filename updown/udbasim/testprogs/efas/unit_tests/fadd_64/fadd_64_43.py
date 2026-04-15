from EFA_v2 import *
def fadd_64_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15362672655965604883, 5777311967423095486]
    tran0.writeAction("movir X16 54579")
    tran0.writeAction("slorii X16 X16 12 726")
    tran0.writeAction("slorii X16 X16 12 699")
    tran0.writeAction("slorii X16 X16 12 1788")
    tran0.writeAction("slorii X16 X16 12 3091")
    tran0.writeAction("movir X17 20525")
    tran0.writeAction("slorii X17 X17 12 553")
    tran0.writeAction("slorii X17 X17 12 4086")
    tran0.writeAction("slorii X17 X17 12 3550")
    tran0.writeAction("slorii X17 X17 12 702")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
