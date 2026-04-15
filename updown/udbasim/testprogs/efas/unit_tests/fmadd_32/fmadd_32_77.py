from EFA_v2 import *
def fmadd_32_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4147824388, 323271120, 3026697998]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 247")
    tran0.writeAction("slorii X16 X16 12 940")
    tran0.writeAction("slorii X16 X16 12 1796")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 19")
    tran0.writeAction("slorii X17 X17 12 1099")
    tran0.writeAction("slorii X17 X17 12 2512")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 180")
    tran0.writeAction("slorii X18 X18 12 1659")
    tran0.writeAction("slorii X18 X18 12 3854")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
