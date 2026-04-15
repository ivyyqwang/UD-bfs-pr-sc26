from EFA_v2 import *
def fdiv_64_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1159229433693412686, 11185235108838277379]
    tran0.writeAction("movir X16 4118")
    tran0.writeAction("slorii X16 X16 12 1680")
    tran0.writeAction("slorii X16 X16 12 1840")
    tran0.writeAction("slorii X16 X16 12 1937")
    tran0.writeAction("slorii X16 X16 12 3406")
    tran0.writeAction("movir X17 39737")
    tran0.writeAction("slorii X17 X17 12 3841")
    tran0.writeAction("slorii X17 X17 12 463")
    tran0.writeAction("slorii X17 X17 12 2184")
    tran0.writeAction("slorii X17 X17 12 259")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
