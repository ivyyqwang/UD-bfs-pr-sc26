from EFA_v2 import *
def fadd_64_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16871474839990056745, 10487840792853594705]
    tran0.writeAction("movir X16 59939")
    tran0.writeAction("slorii X16 X16 12 2127")
    tran0.writeAction("slorii X16 X16 12 2658")
    tran0.writeAction("slorii X16 X16 12 2243")
    tran0.writeAction("slorii X16 X16 12 1833")
    tran0.writeAction("movir X17 37260")
    tran0.writeAction("slorii X17 X17 12 1210")
    tran0.writeAction("slorii X17 X17 12 598")
    tran0.writeAction("slorii X17 X17 12 3644")
    tran0.writeAction("slorii X17 X17 12 593")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
