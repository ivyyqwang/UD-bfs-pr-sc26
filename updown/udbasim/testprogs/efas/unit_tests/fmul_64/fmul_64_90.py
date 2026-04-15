from EFA_v2 import *
def fmul_64_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6194790711155593078, 14863781465254746122]
    tran0.writeAction("movir X16 22008")
    tran0.writeAction("slorii X16 X16 12 1301")
    tran0.writeAction("slorii X16 X16 12 1172")
    tran0.writeAction("slorii X16 X16 12 1304")
    tran0.writeAction("slorii X16 X16 12 3958")
    tran0.writeAction("movir X17 52806")
    tran0.writeAction("slorii X17 X17 12 3111")
    tran0.writeAction("slorii X17 X17 12 3503")
    tran0.writeAction("slorii X17 X17 12 2229")
    tran0.writeAction("slorii X17 X17 12 2058")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
