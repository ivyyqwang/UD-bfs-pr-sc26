from EFA_v2 import *
def fsub_64_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14963091699208902996, 4875520705099891479]
    tran0.writeAction("movir X16 53159")
    tran0.writeAction("slorii X16 X16 12 2377")
    tran0.writeAction("slorii X16 X16 12 3936")
    tran0.writeAction("slorii X16 X16 12 3861")
    tran0.writeAction("slorii X16 X16 12 2388")
    tran0.writeAction("movir X17 17321")
    tran0.writeAction("slorii X17 X17 12 1347")
    tran0.writeAction("slorii X17 X17 12 4074")
    tran0.writeAction("slorii X17 X17 12 2216")
    tran0.writeAction("slorii X17 X17 12 791")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
