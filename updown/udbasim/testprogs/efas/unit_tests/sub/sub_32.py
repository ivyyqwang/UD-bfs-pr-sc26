from EFA_v2 import *
def sub_32():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4080205964820018994, -6073049241827154083]
    tran0.writeAction("movir X16 51040")
    tran0.writeAction("slorii X16 X16 12 804")
    tran0.writeAction("slorii X16 X16 12 2808")
    tran0.writeAction("slorii X16 X16 12 1936")
    tran0.writeAction("slorii X16 X16 12 2254")
    tran0.writeAction("movir X17 43960")
    tran0.writeAction("slorii X17 X17 12 798")
    tran0.writeAction("slorii X17 X17 12 1045")
    tran0.writeAction("slorii X17 X17 12 1790")
    tran0.writeAction("slorii X17 X17 12 1885")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
