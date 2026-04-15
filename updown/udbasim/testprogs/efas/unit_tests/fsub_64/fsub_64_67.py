from EFA_v2 import *
def fsub_64_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8286052572455323787, 15620389946231621466]
    tran0.writeAction("movir X16 29437")
    tran0.writeAction("slorii X16 X16 12 3982")
    tran0.writeAction("slorii X16 X16 12 2507")
    tran0.writeAction("slorii X16 X16 12 1684")
    tran0.writeAction("slorii X16 X16 12 2187")
    tran0.writeAction("movir X17 55494")
    tran0.writeAction("slorii X17 X17 12 3166")
    tran0.writeAction("slorii X17 X17 12 1358")
    tran0.writeAction("slorii X17 X17 12 896")
    tran0.writeAction("slorii X17 X17 12 1882")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
