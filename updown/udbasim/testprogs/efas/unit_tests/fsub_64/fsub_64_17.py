from EFA_v2 import *
def fsub_64_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9356018618704988745, 3256138497120371198]
    tran0.writeAction("movir X16 33239")
    tran0.writeAction("slorii X16 X16 12 1045")
    tran0.writeAction("slorii X16 X16 12 3335")
    tran0.writeAction("slorii X16 X16 12 3488")
    tran0.writeAction("slorii X16 X16 12 2633")
    tran0.writeAction("movir X17 11568")
    tran0.writeAction("slorii X17 X17 12 523")
    tran0.writeAction("slorii X17 X17 12 1564")
    tran0.writeAction("slorii X17 X17 12 1368")
    tran0.writeAction("slorii X17 X17 12 510")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
