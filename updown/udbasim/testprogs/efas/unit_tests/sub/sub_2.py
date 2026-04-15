from EFA_v2 import *
def sub_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7849832518516361911, -2945032133563529980]
    tran0.writeAction("movir X16 27888")
    tran0.writeAction("slorii X16 X16 12 849")
    tran0.writeAction("slorii X16 X16 12 1500")
    tran0.writeAction("slorii X16 X16 12 1956")
    tran0.writeAction("slorii X16 X16 12 2743")
    tran0.writeAction("movir X17 55073")
    tran0.writeAction("slorii X17 X17 12 590")
    tran0.writeAction("slorii X17 X17 12 194")
    tran0.writeAction("slorii X17 X17 12 3420")
    tran0.writeAction("slorii X17 X17 12 1284")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
