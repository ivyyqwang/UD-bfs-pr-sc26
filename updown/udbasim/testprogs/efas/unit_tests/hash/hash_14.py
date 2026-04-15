from EFA_v2 import *
def hash_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2312409797318206368, -1908029960224131745]
    tran0.writeAction("movir X16 8215")
    tran0.writeAction("slorii X16 X16 12 1351")
    tran0.writeAction("slorii X16 X16 12 1408")
    tran0.writeAction("slorii X16 X16 12 1166")
    tran0.writeAction("slorii X16 X16 12 928")
    tran0.writeAction("movir X17 58757")
    tran0.writeAction("slorii X17 X17 12 1293")
    tran0.writeAction("slorii X17 X17 12 3136")
    tran0.writeAction("slorii X17 X17 12 155")
    tran0.writeAction("slorii X17 X17 12 1375")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
