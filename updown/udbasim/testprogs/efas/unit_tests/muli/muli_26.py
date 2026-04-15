from EFA_v2 import *
def muli_26():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [99850061188867502, 5797]
    tran0.writeAction("movir X16 354")
    tran0.writeAction("slorii X16 X16 12 3025")
    tran0.writeAction("slorii X16 X16 12 2563")
    tran0.writeAction("slorii X16 X16 12 3946")
    tran0.writeAction("slorii X16 X16 12 1454")
    tran0.writeAction("muli X16 X17 5797")
    tran0.writeAction("yieldt")
    return efa
