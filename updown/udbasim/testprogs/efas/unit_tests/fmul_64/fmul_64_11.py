from EFA_v2 import *
def fmul_64_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11490461699689516958, 7263687529751493684]
    tran0.writeAction("movir X16 40822")
    tran0.writeAction("slorii X16 X16 12 1312")
    tran0.writeAction("slorii X16 X16 12 2411")
    tran0.writeAction("slorii X16 X16 12 920")
    tran0.writeAction("slorii X16 X16 12 3998")
    tran0.writeAction("movir X17 25805")
    tran0.writeAction("slorii X17 X17 12 3285")
    tran0.writeAction("slorii X17 X17 12 730")
    tran0.writeAction("slorii X17 X17 12 1115")
    tran0.writeAction("slorii X17 X17 12 3124")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
