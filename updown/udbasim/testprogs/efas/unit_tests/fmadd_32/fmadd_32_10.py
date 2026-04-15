from EFA_v2 import *
def fmadd_32_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4105328679, 3816719663, 1902484859]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 244")
    tran0.writeAction("slorii X16 X16 12 2853")
    tran0.writeAction("slorii X16 X16 12 2087")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 227")
    tran0.writeAction("slorii X17 X17 12 2024")
    tran0.writeAction("slorii X17 X17 12 1327")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 113")
    tran0.writeAction("slorii X18 X18 12 1625")
    tran0.writeAction("slorii X18 X18 12 3451")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
