from EFA_v2 import *
def fmul_64_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6024615293311059283, 9988325320643384984]
    tran0.writeAction("movir X16 21403")
    tran0.writeAction("slorii X16 X16 12 3003")
    tran0.writeAction("slorii X16 X16 12 130")
    tran0.writeAction("slorii X16 X16 12 784")
    tran0.writeAction("slorii X16 X16 12 1363")
    tran0.writeAction("movir X17 35485")
    tran0.writeAction("slorii X17 X17 12 2703")
    tran0.writeAction("slorii X17 X17 12 1389")
    tran0.writeAction("slorii X17 X17 12 4049")
    tran0.writeAction("slorii X17 X17 12 1688")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
