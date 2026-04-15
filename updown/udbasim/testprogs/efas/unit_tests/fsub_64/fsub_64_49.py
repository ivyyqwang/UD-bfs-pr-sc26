from EFA_v2 import *
def fsub_64_49():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9021597875185404326, 11517449125904363438]
    tran0.writeAction("movir X16 32051")
    tran0.writeAction("slorii X16 X16 12 631")
    tran0.writeAction("slorii X16 X16 12 2064")
    tran0.writeAction("slorii X16 X16 12 3460")
    tran0.writeAction("slorii X16 X16 12 2470")
    tran0.writeAction("movir X17 40918")
    tran0.writeAction("slorii X17 X17 12 815")
    tran0.writeAction("slorii X17 X17 12 1340")
    tran0.writeAction("slorii X17 X17 12 666")
    tran0.writeAction("slorii X17 X17 12 4014")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
