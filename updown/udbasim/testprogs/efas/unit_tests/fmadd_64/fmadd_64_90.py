from EFA_v2 import *
def fmadd_64_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15336533869237271049, 7071769474432775105, 14795601577915641676]
    tran0.writeAction("movir X16 54486")
    tran0.writeAction("slorii X16 X16 12 1284")
    tran0.writeAction("slorii X16 X16 12 3121")
    tran0.writeAction("slorii X16 X16 12 2599")
    tran0.writeAction("slorii X16 X16 12 2569")
    tran0.writeAction("movir X17 25123")
    tran0.writeAction("slorii X17 X17 12 3981")
    tran0.writeAction("slorii X17 X17 12 3713")
    tran0.writeAction("slorii X17 X17 12 67")
    tran0.writeAction("slorii X17 X17 12 961")
    tran0.writeAction("movir X18 52564")
    tran0.writeAction("slorii X18 X18 12 2195")
    tran0.writeAction("slorii X18 X18 12 3745")
    tran0.writeAction("slorii X18 X18 12 3566")
    tran0.writeAction("slorii X18 X18 12 3916")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
