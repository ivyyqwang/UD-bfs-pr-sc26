from EFA_v2 import *
def fsub_64_50():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14518012902942160950, 11034840716496707366]
    tran0.writeAction("movir X16 51578")
    tran0.writeAction("slorii X16 X16 12 1405")
    tran0.writeAction("slorii X16 X16 12 196")
    tran0.writeAction("slorii X16 X16 12 1659")
    tran0.writeAction("slorii X16 X16 12 2102")
    tran0.writeAction("movir X17 39203")
    tran0.writeAction("slorii X17 X17 12 2578")
    tran0.writeAction("slorii X17 X17 12 2723")
    tran0.writeAction("slorii X17 X17 12 3289")
    tran0.writeAction("slorii X17 X17 12 3878")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
