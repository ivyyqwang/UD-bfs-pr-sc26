from EFA_v2 import *
def fmadd_32_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [345445695, 1166145377, 1783994015]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 20")
    tran0.writeAction("slorii X16 X16 12 2417")
    tran0.writeAction("slorii X16 X16 12 1343")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 69")
    tran0.writeAction("slorii X17 X17 12 2079")
    tran0.writeAction("slorii X17 X17 12 1889")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 106")
    tran0.writeAction("slorii X18 X18 12 1369")
    tran0.writeAction("slorii X18 X18 12 1695")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
