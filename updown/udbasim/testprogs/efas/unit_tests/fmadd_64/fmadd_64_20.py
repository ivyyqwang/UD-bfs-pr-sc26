from EFA_v2 import *
def fmadd_64_20():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11749323411634192308, 17315862579277754541, 13641113207927128310]
    tran0.writeAction("movir X16 41741")
    tran0.writeAction("slorii X16 X16 12 4022")
    tran0.writeAction("slorii X16 X16 12 1133")
    tran0.writeAction("slorii X16 X16 12 2607")
    tran0.writeAction("slorii X16 X16 12 4020")
    tran0.writeAction("movir X17 61518")
    tran0.writeAction("slorii X17 X17 12 1236")
    tran0.writeAction("slorii X17 X17 12 1473")
    tran0.writeAction("slorii X17 X17 12 1351")
    tran0.writeAction("slorii X17 X17 12 173")
    tran0.writeAction("movir X18 48462")
    tran0.writeAction("slorii X18 X18 12 3971")
    tran0.writeAction("slorii X18 X18 12 91")
    tran0.writeAction("slorii X18 X18 12 1580")
    tran0.writeAction("slorii X18 X18 12 246")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
