from EFA_v2 import *
def fmadd_32_46():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1529261617, 4030737112, 3945448975]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 91")
    tran0.writeAction("slorii X16 X16 12 618")
    tran0.writeAction("slorii X16 X16 12 3633")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 240")
    tran0.writeAction("slorii X17 X17 12 1026")
    tran0.writeAction("slorii X17 X17 12 2776")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 235")
    tran0.writeAction("slorii X18 X18 12 684")
    tran0.writeAction("slorii X18 X18 12 1551")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
