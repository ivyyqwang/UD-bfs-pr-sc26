from EFA_v2 import *
def hash_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6168580712114720610, -4604929583303463001]
    tran0.writeAction("movir X16 21915")
    tran0.writeAction("slorii X16 X16 12 823")
    tran0.writeAction("slorii X16 X16 12 2465")
    tran0.writeAction("slorii X16 X16 12 3784")
    tran0.writeAction("slorii X16 X16 12 3938")
    tran0.writeAction("movir X17 49176")
    tran0.writeAction("slorii X17 X17 12 15")
    tran0.writeAction("slorii X17 X17 12 291")
    tran0.writeAction("slorii X17 X17 12 2086")
    tran0.writeAction("slorii X17 X17 12 4007")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
