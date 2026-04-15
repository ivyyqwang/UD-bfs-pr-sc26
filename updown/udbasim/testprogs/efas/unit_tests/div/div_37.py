from EFA_v2 import *
def div_37():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1868631838633978593, -2503680645882393163]
    tran0.writeAction("movir X16 6638")
    tran0.writeAction("slorii X16 X16 12 2924")
    tran0.writeAction("slorii X16 X16 12 445")
    tran0.writeAction("slorii X16 X16 12 3126")
    tran0.writeAction("slorii X16 X16 12 2785")
    tran0.writeAction("movir X17 56641")
    tran0.writeAction("slorii X17 X17 12 571")
    tran0.writeAction("slorii X17 X17 12 1975")
    tran0.writeAction("slorii X17 X17 12 652")
    tran0.writeAction("slorii X17 X17 12 3509")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
