from EFA_v2 import *
def div_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8219148078929523317, 1112316159441370430]
    tran0.writeAction("movir X16 29200")
    tran0.writeAction("slorii X16 X16 12 1146")
    tran0.writeAction("slorii X16 X16 12 384")
    tran0.writeAction("slorii X16 X16 12 3803")
    tran0.writeAction("slorii X16 X16 12 629")
    tran0.writeAction("movir X17 3951")
    tran0.writeAction("slorii X17 X17 12 3034")
    tran0.writeAction("slorii X17 X17 12 1881")
    tran0.writeAction("slorii X17 X17 12 1759")
    tran0.writeAction("slorii X17 X17 12 3390")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
