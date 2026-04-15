from EFA_v2 import *
def subi_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4286607580931206129, -3532]
    tran0.writeAction("movir X16 15229")
    tran0.writeAction("slorii X16 X16 12 366")
    tran0.writeAction("slorii X16 X16 12 552")
    tran0.writeAction("slorii X16 X16 12 3690")
    tran0.writeAction("slorii X16 X16 12 3057")
    tran0.writeAction("subi X16 X17 -3532")
    tran0.writeAction("yieldt")
    return efa
