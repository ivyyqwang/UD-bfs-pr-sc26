from EFA_v2 import *
def fmadd_32_25():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2659389872, 522835657, 2597688979]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 158")
    tran0.writeAction("slorii X16 X16 12 2097")
    tran0.writeAction("slorii X16 X16 12 432")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 31")
    tran0.writeAction("slorii X17 X17 12 669")
    tran0.writeAction("slorii X17 X17 12 1737")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 154")
    tran0.writeAction("slorii X18 X18 12 3417")
    tran0.writeAction("slorii X18 X18 12 1683")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
