from EFA_v2 import *
def fmadd_64_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5723945549923348284, 2309122000517247690, 2406191460744424825]
    tran0.writeAction("movir X16 20335")
    tran0.writeAction("slorii X16 X16 12 2210")
    tran0.writeAction("slorii X16 X16 12 1696")
    tran0.writeAction("slorii X16 X16 12 3518")
    tran0.writeAction("slorii X16 X16 12 3900")
    tran0.writeAction("movir X17 8203")
    tran0.writeAction("slorii X17 X17 12 2659")
    tran0.writeAction("slorii X17 X17 12 2471")
    tran0.writeAction("slorii X17 X17 12 3563")
    tran0.writeAction("slorii X17 X17 12 714")
    tran0.writeAction("movir X18 8548")
    tran0.writeAction("slorii X18 X18 12 2086")
    tran0.writeAction("slorii X18 X18 12 655")
    tran0.writeAction("slorii X18 X18 12 1022")
    tran0.writeAction("slorii X18 X18 12 3449")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
