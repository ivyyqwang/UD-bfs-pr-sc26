from EFA_v2 import *
def addi_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3141129490218814811, -19716]
    tran0.writeAction("movir X16 11159")
    tran0.writeAction("slorii X16 X16 12 2186")
    tran0.writeAction("slorii X16 X16 12 257")
    tran0.writeAction("slorii X16 X16 12 4080")
    tran0.writeAction("slorii X16 X16 12 3419")
    tran0.writeAction("addi X16 X17 -19716")
    tran0.writeAction("yieldt")
    return efa
