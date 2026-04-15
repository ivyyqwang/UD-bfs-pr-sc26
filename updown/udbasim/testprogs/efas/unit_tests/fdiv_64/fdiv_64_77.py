from EFA_v2 import *
def fdiv_64_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17887314434389867661, 5104847086767815247]
    tran0.writeAction("movir X16 63548")
    tran0.writeAction("slorii X16 X16 12 2075")
    tran0.writeAction("slorii X16 X16 12 1279")
    tran0.writeAction("slorii X16 X16 12 2151")
    tran0.writeAction("slorii X16 X16 12 3213")
    tran0.writeAction("movir X17 18136")
    tran0.writeAction("slorii X17 X17 12 246")
    tran0.writeAction("slorii X17 X17 12 247")
    tran0.writeAction("slorii X17 X17 12 1979")
    tran0.writeAction("slorii X17 X17 12 2639")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
