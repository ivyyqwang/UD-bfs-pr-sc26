from EFA_v2 import *
def fmul_64_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16388315846644932524, 4165102381463926831]
    tran0.writeAction("movir X16 58222")
    tran0.writeAction("slorii X16 X16 12 4070")
    tran0.writeAction("slorii X16 X16 12 3834")
    tran0.writeAction("slorii X16 X16 12 721")
    tran0.writeAction("slorii X16 X16 12 4012")
    tran0.writeAction("movir X17 14797")
    tran0.writeAction("slorii X17 X17 12 1704")
    tran0.writeAction("slorii X17 X17 12 3164")
    tran0.writeAction("slorii X17 X17 12 1191")
    tran0.writeAction("slorii X17 X17 12 2095")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
