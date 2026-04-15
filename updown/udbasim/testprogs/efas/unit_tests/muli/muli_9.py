from EFA_v2 import *
def muli_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7687739971398012540, 31123]
    tran0.writeAction("movir X16 27312")
    tran0.writeAction("slorii X16 X16 12 1388")
    tran0.writeAction("slorii X16 X16 12 1480")
    tran0.writeAction("slorii X16 X16 12 3072")
    tran0.writeAction("slorii X16 X16 12 3708")
    tran0.writeAction("muli X16 X17 31123")
    tran0.writeAction("yieldt")
    return efa
