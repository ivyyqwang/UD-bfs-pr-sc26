from EFA_v2 import *
def fmul_64_99():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17838935023546064988, 17193913981861546641]
    tran0.writeAction("movir X16 63376")
    tran0.writeAction("slorii X16 X16 12 2574")
    tran0.writeAction("slorii X16 X16 12 929")
    tran0.writeAction("slorii X16 X16 12 3022")
    tran0.writeAction("slorii X16 X16 12 92")
    tran0.writeAction("movir X17 61085")
    tran0.writeAction("slorii X17 X17 12 218")
    tran0.writeAction("slorii X17 X17 12 2899")
    tran0.writeAction("slorii X17 X17 12 1964")
    tran0.writeAction("slorii X17 X17 12 2705")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
