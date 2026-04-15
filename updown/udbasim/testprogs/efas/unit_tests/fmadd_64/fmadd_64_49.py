from EFA_v2 import *
def fmadd_64_49():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4464972143071604612, 13756613130644173553, 9790808673497999646]
    tran0.writeAction("movir X16 15862")
    tran0.writeAction("slorii X16 X16 12 3144")
    tran0.writeAction("slorii X16 X16 12 503")
    tran0.writeAction("slorii X16 X16 12 3266")
    tran0.writeAction("slorii X16 X16 12 3972")
    tran0.writeAction("movir X17 48873")
    tran0.writeAction("slorii X17 X17 12 1260")
    tran0.writeAction("slorii X17 X17 12 436")
    tran0.writeAction("slorii X17 X17 12 2131")
    tran0.writeAction("slorii X17 X17 12 753")
    tran0.writeAction("movir X18 34783")
    tran0.writeAction("slorii X18 X18 12 3849")
    tran0.writeAction("slorii X18 X18 12 3415")
    tran0.writeAction("slorii X18 X18 12 2710")
    tran0.writeAction("slorii X18 X18 12 2334")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
