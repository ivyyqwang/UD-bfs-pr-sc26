from EFA_v2 import *
def sub_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6744470386272153371, -8752034443903225515]
    tran0.writeAction("movir X16 23961")
    tran0.writeAction("slorii X16 X16 12 705")
    tran0.writeAction("slorii X16 X16 12 1315")
    tran0.writeAction("slorii X16 X16 12 3658")
    tran0.writeAction("slorii X16 X16 12 3867")
    tran0.writeAction("movir X17 34442")
    tran0.writeAction("slorii X17 X17 12 2160")
    tran0.writeAction("slorii X17 X17 12 2853")
    tran0.writeAction("slorii X17 X17 12 675")
    tran0.writeAction("slorii X17 X17 12 341")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
