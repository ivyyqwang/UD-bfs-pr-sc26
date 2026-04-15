from EFA_v2 import *
def mod_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4236419022419483934, 7752596315766876678]
    tran0.writeAction("movir X16 15050")
    tran0.writeAction("slorii X16 X16 12 3210")
    tran0.writeAction("slorii X16 X16 12 1991")
    tran0.writeAction("slorii X16 X16 12 85")
    tran0.writeAction("slorii X16 X16 12 3358")
    tran0.writeAction("movir X17 27542")
    tran0.writeAction("slorii X17 X17 12 3092")
    tran0.writeAction("slorii X17 X17 12 1584")
    tran0.writeAction("slorii X17 X17 12 1174")
    tran0.writeAction("slorii X17 X17 12 2566")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
