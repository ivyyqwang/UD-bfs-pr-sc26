from EFA_v2 import *
def muli_29():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6383546091720267497, 20635]
    tran0.writeAction("movir X16 42857")
    tran0.writeAction("slorii X16 X16 12 362")
    tran0.writeAction("slorii X16 X16 12 1707")
    tran0.writeAction("slorii X16 X16 12 2786")
    tran0.writeAction("slorii X16 X16 12 2327")
    tran0.writeAction("muli X16 X17 20635")
    tran0.writeAction("yieldt")
    return efa
