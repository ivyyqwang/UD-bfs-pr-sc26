from EFA_v2 import *
def fmadd_32_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2260467864, 696802059, 158919794]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 134")
    tran0.writeAction("slorii X16 X16 12 3008")
    tran0.writeAction("slorii X16 X16 12 152")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 41")
    tran0.writeAction("slorii X17 X17 12 2181")
    tran0.writeAction("slorii X17 X17 12 2827")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 9")
    tran0.writeAction("slorii X18 X18 12 1934")
    tran0.writeAction("slorii X18 X18 12 3186")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
