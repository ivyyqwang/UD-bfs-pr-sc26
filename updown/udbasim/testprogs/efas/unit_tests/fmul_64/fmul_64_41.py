from EFA_v2 import *
def fmul_64_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7384020445467323569, 3053700894774237032]
    tran0.writeAction("movir X16 26233")
    tran0.writeAction("slorii X16 X16 12 1271")
    tran0.writeAction("slorii X16 X16 12 2322")
    tran0.writeAction("slorii X16 X16 12 1234")
    tran0.writeAction("slorii X16 X16 12 3249")
    tran0.writeAction("movir X17 10848")
    tran0.writeAction("slorii X17 X17 12 3788")
    tran0.writeAction("slorii X17 X17 12 2267")
    tran0.writeAction("slorii X17 X17 12 1273")
    tran0.writeAction("slorii X17 X17 12 1896")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
