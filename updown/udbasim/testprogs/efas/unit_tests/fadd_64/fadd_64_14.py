from EFA_v2 import *
def fadd_64_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5399694549957778209, 16239259548145278993]
    tran0.writeAction("movir X16 19183")
    tran0.writeAction("slorii X16 X16 12 2329")
    tran0.writeAction("slorii X16 X16 12 1433")
    tran0.writeAction("slorii X16 X16 12 3465")
    tran0.writeAction("slorii X16 X16 12 2849")
    tran0.writeAction("movir X17 57693")
    tran0.writeAction("slorii X17 X17 12 1800")
    tran0.writeAction("slorii X17 X17 12 1294")
    tran0.writeAction("slorii X17 X17 12 2334")
    tran0.writeAction("slorii X17 X17 12 17")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
