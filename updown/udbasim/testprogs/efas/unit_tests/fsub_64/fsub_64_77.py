from EFA_v2 import *
def fsub_64_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14545062851929773954, 10801491567414053786]
    tran0.writeAction("movir X16 51674")
    tran0.writeAction("slorii X16 X16 12 1817")
    tran0.writeAction("slorii X16 X16 12 2509")
    tran0.writeAction("slorii X16 X16 12 17")
    tran0.writeAction("slorii X16 X16 12 1922")
    tran0.writeAction("movir X17 38374")
    tran0.writeAction("slorii X17 X17 12 2485")
    tran0.writeAction("slorii X17 X17 12 2576")
    tran0.writeAction("slorii X17 X17 12 376")
    tran0.writeAction("slorii X17 X17 12 2970")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
