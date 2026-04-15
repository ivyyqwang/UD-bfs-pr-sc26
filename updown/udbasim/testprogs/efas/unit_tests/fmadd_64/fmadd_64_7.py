from EFA_v2 import *
def fmadd_64_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1103927136141461617, 17993287710915852023, 4092807628505111549]
    tran0.writeAction("movir X16 3921")
    tran0.writeAction("slorii X16 X16 12 3838")
    tran0.writeAction("slorii X16 X16 12 423")
    tran0.writeAction("slorii X16 X16 12 2564")
    tran0.writeAction("slorii X16 X16 12 2161")
    tran0.writeAction("movir X17 63924")
    tran0.writeAction("slorii X17 X17 12 4093")
    tran0.writeAction("slorii X17 X17 12 1838")
    tran0.writeAction("slorii X17 X17 12 2215")
    tran0.writeAction("slorii X17 X17 12 1783")
    tran0.writeAction("movir X18 14540")
    tran0.writeAction("slorii X18 X18 12 2349")
    tran0.writeAction("slorii X18 X18 12 2687")
    tran0.writeAction("slorii X18 X18 12 229")
    tran0.writeAction("slorii X18 X18 12 3069")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
