from EFA_v2 import *
def fmul_64_78():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16497688013204299011, 16081521041439441807]
    tran0.writeAction("movir X16 58611")
    tran0.writeAction("slorii X16 X16 12 2301")
    tran0.writeAction("slorii X16 X16 12 1770")
    tran0.writeAction("slorii X16 X16 12 1073")
    tran0.writeAction("slorii X16 X16 12 3331")
    tran0.writeAction("movir X17 57133")
    tran0.writeAction("slorii X17 X17 12 162")
    tran0.writeAction("slorii X17 X17 12 3842")
    tran0.writeAction("slorii X17 X17 12 3964")
    tran0.writeAction("slorii X17 X17 12 911")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
