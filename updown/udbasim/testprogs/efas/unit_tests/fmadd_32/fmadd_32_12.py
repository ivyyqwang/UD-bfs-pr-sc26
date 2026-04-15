from EFA_v2 import *
def fmadd_32_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1050901408, 3330810323, 3525751747]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 62")
    tran0.writeAction("slorii X16 X16 12 2615")
    tran0.writeAction("slorii X16 X16 12 2976")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 198")
    tran0.writeAction("slorii X17 X17 12 2178")
    tran0.writeAction("slorii X17 X17 12 467")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 210")
    tran0.writeAction("slorii X18 X18 12 619")
    tran0.writeAction("slorii X18 X18 12 963")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
