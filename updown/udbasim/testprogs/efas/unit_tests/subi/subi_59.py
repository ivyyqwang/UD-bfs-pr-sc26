from EFA_v2 import *
def subi_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8216131414539930849, 18740]
    tran0.writeAction("movir X16 29189")
    tran0.writeAction("slorii X16 X16 12 2303")
    tran0.writeAction("slorii X16 X16 12 3479")
    tran0.writeAction("slorii X16 X16 12 2376")
    tran0.writeAction("slorii X16 X16 12 3297")
    tran0.writeAction("subi X16 X17 18740")
    tran0.writeAction("yieldt")
    return efa
