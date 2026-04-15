from EFA_v2 import *
def fmadd_32_99():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1362678515, 912850539, 848221962]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 81")
    tran0.writeAction("slorii X16 X16 12 909")
    tran0.writeAction("slorii X16 X16 12 755")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 54")
    tran0.writeAction("slorii X17 X17 12 1679")
    tran0.writeAction("slorii X17 X17 12 3691")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 50")
    tran0.writeAction("slorii X18 X18 12 2285")
    tran0.writeAction("slorii X18 X18 12 1802")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
