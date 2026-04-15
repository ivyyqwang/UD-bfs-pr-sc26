from EFA_v2 import *
def sub_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4801857990735876360, 41760394249562043]
    tran0.writeAction("movir X16 48476")
    tran0.writeAction("slorii X16 X16 12 1529")
    tran0.writeAction("slorii X16 X16 12 2376")
    tran0.writeAction("slorii X16 X16 12 1298")
    tran0.writeAction("slorii X16 X16 12 3832")
    tran0.writeAction("movir X17 148")
    tran0.writeAction("slorii X17 X17 12 1485")
    tran0.writeAction("slorii X17 X17 12 2936")
    tran0.writeAction("slorii X17 X17 12 3790")
    tran0.writeAction("slorii X17 X17 12 1979")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
