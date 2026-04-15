from EFA_v2 import *
def fmadd_32_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1081473594, 100575885, 1583260860]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 64")
    tran0.writeAction("slorii X16 X16 12 1887")
    tran0.writeAction("slorii X16 X16 12 2618")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 5")
    tran0.writeAction("slorii X17 X17 12 4074")
    tran0.writeAction("slorii X17 X17 12 2701")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 94")
    tran0.writeAction("slorii X18 X18 12 1514")
    tran0.writeAction("slorii X18 X18 12 1212")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
