from EFA_v2 import *
def fsub_64_62():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1945051318014888870, 1541295562881443709]
    tran0.writeAction("movir X16 6910")
    tran0.writeAction("slorii X16 X16 12 861")
    tran0.writeAction("slorii X16 X16 12 3664")
    tran0.writeAction("slorii X16 X16 12 748")
    tran0.writeAction("slorii X16 X16 12 2982")
    tran0.writeAction("movir X17 5475")
    tran0.writeAction("slorii X17 X17 12 3202")
    tran0.writeAction("slorii X17 X17 12 1527")
    tran0.writeAction("slorii X17 X17 12 1778")
    tran0.writeAction("slorii X17 X17 12 1917")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
