from EFA_v2 import *
def fsub_64_82():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16431702792066396240, 6413572950976231389]
    tran0.writeAction("movir X16 58377")
    tran0.writeAction("slorii X16 X16 12 554")
    tran0.writeAction("slorii X16 X16 12 359")
    tran0.writeAction("slorii X16 X16 12 3735")
    tran0.writeAction("slorii X16 X16 12 80")
    tran0.writeAction("movir X17 22785")
    tran0.writeAction("slorii X17 X17 12 2409")
    tran0.writeAction("slorii X17 X17 12 3659")
    tran0.writeAction("slorii X17 X17 12 4063")
    tran0.writeAction("slorii X17 X17 12 2013")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
