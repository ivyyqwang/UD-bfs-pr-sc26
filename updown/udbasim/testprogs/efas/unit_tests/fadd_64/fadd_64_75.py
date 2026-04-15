from EFA_v2 import *
def fadd_64_75():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10665773247263945505, 134496300286266043]
    tran0.writeAction("movir X16 37892")
    tran0.writeAction("slorii X16 X16 12 1796")
    tran0.writeAction("slorii X16 X16 12 570")
    tran0.writeAction("slorii X16 X16 12 131")
    tran0.writeAction("slorii X16 X16 12 801")
    tran0.writeAction("movir X17 477")
    tran0.writeAction("slorii X17 X17 12 3386")
    tran0.writeAction("slorii X17 X17 12 3114")
    tran0.writeAction("slorii X17 X17 12 684")
    tran0.writeAction("slorii X17 X17 12 2747")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
