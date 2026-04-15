from EFA_v2 import *
def fmadd_32_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4265797713, 1290201366, 3605132058]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 254")
    tran0.writeAction("slorii X16 X16 12 1070")
    tran0.writeAction("slorii X16 X16 12 2129")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 76")
    tran0.writeAction("slorii X17 X17 12 3694")
    tran0.writeAction("slorii X17 X17 12 2326")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 214")
    tran0.writeAction("slorii X18 X18 12 3615")
    tran0.writeAction("slorii X18 X18 12 794")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
