from EFA_v2 import *
def fdiv_64_88():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11353636534979932409, 13945137319652000092]
    tran0.writeAction("movir X16 40336")
    tran0.writeAction("slorii X16 X16 12 900")
    tran0.writeAction("slorii X16 X16 12 1600")
    tran0.writeAction("slorii X16 X16 12 1539")
    tran0.writeAction("slorii X16 X16 12 249")
    tran0.writeAction("movir X17 49543")
    tran0.writeAction("slorii X17 X17 12 328")
    tran0.writeAction("slorii X17 X17 12 505")
    tran0.writeAction("slorii X17 X17 12 3688")
    tran0.writeAction("slorii X17 X17 12 348")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
