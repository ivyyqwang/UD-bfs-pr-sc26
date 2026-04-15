from EFA_v2 import *
def sub_23():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3347340985305613425, 6101454718883369103]
    tran0.writeAction("movir X16 11892")
    tran0.writeAction("slorii X16 X16 12 590")
    tran0.writeAction("slorii X16 X16 12 1059")
    tran0.writeAction("slorii X16 X16 12 1012")
    tran0.writeAction("slorii X16 X16 12 1137")
    tran0.writeAction("movir X17 21676")
    tran0.writeAction("slorii X17 X17 12 2955")
    tran0.writeAction("slorii X17 X17 12 3436")
    tran0.writeAction("slorii X17 X17 12 713")
    tran0.writeAction("slorii X17 X17 12 143")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
