from EFA_v2 import *
def fdiv_64_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6082277869214704424, 1608125798887860513]
    tran0.writeAction("movir X16 21608")
    tran0.writeAction("slorii X16 X16 12 2423")
    tran0.writeAction("slorii X16 X16 12 3883")
    tran0.writeAction("slorii X16 X16 12 3122")
    tran0.writeAction("slorii X16 X16 12 808")
    tran0.writeAction("movir X17 5713")
    tran0.writeAction("slorii X17 X17 12 862")
    tran0.writeAction("slorii X17 X17 12 1236")
    tran0.writeAction("slorii X17 X17 12 3490")
    tran0.writeAction("slorii X17 X17 12 2337")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
