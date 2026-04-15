from EFA_v2 import *
def subi_75():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7627456215671048494, -23473]
    tran0.writeAction("movir X16 38437")
    tran0.writeAction("slorii X16 X16 12 3407")
    tran0.writeAction("slorii X16 X16 12 3037")
    tran0.writeAction("slorii X16 X16 12 335")
    tran0.writeAction("slorii X16 X16 12 1746")
    tran0.writeAction("subi X16 X17 -23473")
    tran0.writeAction("yieldt")
    return efa
