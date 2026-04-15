from EFA_v2 import *
def subi_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7690160143930849026, -32686]
    tran0.writeAction("movir X16 38215")
    tran0.writeAction("slorii X16 X16 12 257")
    tran0.writeAction("slorii X16 X16 12 2019")
    tran0.writeAction("slorii X16 X16 12 552")
    tran0.writeAction("slorii X16 X16 12 2302")
    tran0.writeAction("subi X16 X17 -32686")
    tran0.writeAction("yieldt")
    return efa
