from EFA_v2 import *
def fmadd_64_28():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4769974716483211885, 1513550861943009864, 10810402513218896444]
    tran0.writeAction("movir X16 16946")
    tran0.writeAction("slorii X16 X16 12 1451")
    tran0.writeAction("slorii X16 X16 12 2931")
    tran0.writeAction("slorii X16 X16 12 2361")
    tran0.writeAction("slorii X16 X16 12 621")
    tran0.writeAction("movir X17 5377")
    tran0.writeAction("slorii X17 X17 12 871")
    tran0.writeAction("slorii X17 X17 12 3427")
    tran0.writeAction("slorii X17 X17 12 2455")
    tran0.writeAction("slorii X17 X17 12 584")
    tran0.writeAction("movir X18 38406")
    tran0.writeAction("slorii X18 X18 12 1084")
    tran0.writeAction("slorii X18 X18 12 3919")
    tran0.writeAction("slorii X18 X18 12 1648")
    tran0.writeAction("slorii X18 X18 12 572")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
