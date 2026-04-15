from EFA_v2 import *
def fadd_64_44():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8962609609326717426, 3008009405790783268]
    tran0.writeAction("movir X16 31841")
    tran0.writeAction("slorii X16 X16 12 2399")
    tran0.writeAction("slorii X16 X16 12 1064")
    tran0.writeAction("slorii X16 X16 12 1726")
    tran0.writeAction("slorii X16 X16 12 2546")
    tran0.writeAction("movir X17 10686")
    tran0.writeAction("slorii X17 X17 12 2441")
    tran0.writeAction("slorii X17 X17 12 3601")
    tran0.writeAction("slorii X17 X17 12 792")
    tran0.writeAction("slorii X17 X17 12 1828")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
