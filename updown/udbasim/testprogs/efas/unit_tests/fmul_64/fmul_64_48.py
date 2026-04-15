from EFA_v2 import *
def fmul_64_48():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1634392746452326578, 5415232854779637473]
    tran0.writeAction("movir X16 5806")
    tran0.writeAction("slorii X16 X16 12 2168")
    tran0.writeAction("slorii X16 X16 12 2851")
    tran0.writeAction("slorii X16 X16 12 3137")
    tran0.writeAction("slorii X16 X16 12 2226")
    tran0.writeAction("movir X17 19238")
    tran0.writeAction("slorii X17 X17 12 3161")
    tran0.writeAction("slorii X17 X17 12 1821")
    tran0.writeAction("slorii X17 X17 12 674")
    tran0.writeAction("slorii X17 X17 12 3809")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
