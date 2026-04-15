from EFA_v2 import *
def div_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1748043403922807022, 8669276161812138396]
    tran0.writeAction("movir X16 59325")
    tran0.writeAction("slorii X16 X16 12 2876")
    tran0.writeAction("slorii X16 X16 12 2337")
    tran0.writeAction("slorii X16 X16 12 886")
    tran0.writeAction("slorii X16 X16 12 1810")
    tran0.writeAction("movir X17 30799")
    tran0.writeAction("slorii X17 X17 12 1867")
    tran0.writeAction("slorii X17 X17 12 3268")
    tran0.writeAction("slorii X17 X17 12 2352")
    tran0.writeAction("slorii X17 X17 12 2460")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
