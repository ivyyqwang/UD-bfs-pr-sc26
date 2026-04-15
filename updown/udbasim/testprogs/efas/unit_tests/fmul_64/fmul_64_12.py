from EFA_v2 import *
def fmul_64_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6058500451866764825, 17723949096634263923]
    tran0.writeAction("movir X16 21524")
    tran0.writeAction("slorii X16 X16 12 480")
    tran0.writeAction("slorii X16 X16 12 4041")
    tran0.writeAction("slorii X16 X16 12 254")
    tran0.writeAction("slorii X16 X16 12 1561")
    tran0.writeAction("movir X17 62968")
    tran0.writeAction("slorii X17 X17 12 476")
    tran0.writeAction("slorii X17 X17 12 3137")
    tran0.writeAction("slorii X17 X17 12 4058")
    tran0.writeAction("slorii X17 X17 12 2419")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
