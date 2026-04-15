from EFA_v2 import *
def subi_92():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6847059797940700422, 16901]
    tran0.writeAction("movir X16 24325")
    tran0.writeAction("slorii X16 X16 12 2633")
    tran0.writeAction("slorii X16 X16 12 3044")
    tran0.writeAction("slorii X16 X16 12 464")
    tran0.writeAction("slorii X16 X16 12 1286")
    tran0.writeAction("subi X16 X17 16901")
    tran0.writeAction("yieldt")
    return efa
