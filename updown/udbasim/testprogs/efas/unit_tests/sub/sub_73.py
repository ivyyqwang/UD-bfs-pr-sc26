from EFA_v2 import *
def sub_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1830314432360611864, -5120398312127266771]
    tran0.writeAction("movir X16 6502")
    tran0.writeAction("slorii X16 X16 12 2388")
    tran0.writeAction("slorii X16 X16 12 1888")
    tran0.writeAction("slorii X16 X16 12 512")
    tran0.writeAction("slorii X16 X16 12 24")
    tran0.writeAction("movir X17 47344")
    tran0.writeAction("slorii X17 X17 12 2829")
    tran0.writeAction("slorii X17 X17 12 3385")
    tran0.writeAction("slorii X17 X17 12 592")
    tran0.writeAction("slorii X17 X17 12 45")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
