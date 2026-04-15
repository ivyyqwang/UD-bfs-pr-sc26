from EFA_v2 import *
def fmadd_64_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9784348955444755509, 7206694301959645171, 15048385584375796581]
    tran0.writeAction("movir X16 34760")
    tran0.writeAction("slorii X16 X16 12 4056")
    tran0.writeAction("slorii X16 X16 12 2311")
    tran0.writeAction("slorii X16 X16 12 3067")
    tran0.writeAction("slorii X16 X16 12 3125")
    tran0.writeAction("movir X17 25603")
    tran0.writeAction("slorii X17 X17 12 1316")
    tran0.writeAction("slorii X17 X17 12 2289")
    tran0.writeAction("slorii X17 X17 12 558")
    tran0.writeAction("slorii X17 X17 12 2035")
    tran0.writeAction("movir X18 53462")
    tran0.writeAction("slorii X18 X18 12 2479")
    tran0.writeAction("slorii X18 X18 12 1423")
    tran0.writeAction("slorii X18 X18 12 3393")
    tran0.writeAction("slorii X18 X18 12 869")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
