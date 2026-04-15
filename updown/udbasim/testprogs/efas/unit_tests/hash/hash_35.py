from EFA_v2 import *
def hash_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8409195064756146547, 2688448345892844598]
    tran0.writeAction("movir X16 35660")
    tran0.writeAction("slorii X16 X16 12 2202")
    tran0.writeAction("slorii X16 X16 12 1142")
    tran0.writeAction("slorii X16 X16 12 990")
    tran0.writeAction("slorii X16 X16 12 3725")
    tran0.writeAction("movir X17 9551")
    tran0.writeAction("slorii X17 X17 12 1176")
    tran0.writeAction("slorii X17 X17 12 1741")
    tran0.writeAction("slorii X17 X17 12 3807")
    tran0.writeAction("slorii X17 X17 12 1078")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
