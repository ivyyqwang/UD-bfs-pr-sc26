from EFA_v2 import *
def fadd_64_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7816375613192441013, 18329626020018916505]
    tran0.writeAction("movir X16 27769")
    tran0.writeAction("slorii X16 X16 12 1411")
    tran0.writeAction("slorii X16 X16 12 1295")
    tran0.writeAction("slorii X16 X16 12 1480")
    tran0.writeAction("slorii X16 X16 12 3253")
    tran0.writeAction("movir X17 65119")
    tran0.writeAction("slorii X17 X17 12 3740")
    tran0.writeAction("slorii X17 X17 12 44")
    tran0.writeAction("slorii X17 X17 12 4032")
    tran0.writeAction("slorii X17 X17 12 3225")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
