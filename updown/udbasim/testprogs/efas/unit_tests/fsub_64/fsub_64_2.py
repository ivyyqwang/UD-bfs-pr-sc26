from EFA_v2 import *
def fsub_64_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11481769888931791463, 10034326246055709053]
    tran0.writeAction("movir X16 40791")
    tran0.writeAction("slorii X16 X16 12 1806")
    tran0.writeAction("slorii X16 X16 12 390")
    tran0.writeAction("slorii X16 X16 12 2276")
    tran0.writeAction("slorii X16 X16 12 615")
    tran0.writeAction("movir X17 35649")
    tran0.writeAction("slorii X17 X17 12 360")
    tran0.writeAction("slorii X17 X17 12 3712")
    tran0.writeAction("slorii X17 X17 12 2168")
    tran0.writeAction("slorii X17 X17 12 2429")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
