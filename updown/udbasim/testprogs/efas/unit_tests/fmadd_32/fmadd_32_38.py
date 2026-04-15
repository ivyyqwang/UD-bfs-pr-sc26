from EFA_v2 import *
def fmadd_32_38():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [337928668, 3130820339, 145965720]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 20")
    tran0.writeAction("slorii X16 X16 12 582")
    tran0.writeAction("slorii X16 X16 12 476")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 186")
    tran0.writeAction("slorii X17 X17 12 2504")
    tran0.writeAction("slorii X17 X17 12 1779")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 8")
    tran0.writeAction("slorii X18 X18 12 2868")
    tran0.writeAction("slorii X18 X18 12 664")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
