from EFA_v2 import *
def mul_93():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2942431244389862932, 2260170499450750357]
    tran0.writeAction("movir X16 10453")
    tran0.writeAction("slorii X16 X16 12 2522")
    tran0.writeAction("slorii X16 X16 12 137")
    tran0.writeAction("slorii X16 X16 12 3556")
    tran0.writeAction("slorii X16 X16 12 3604")
    tran0.writeAction("movir X17 8029")
    tran0.writeAction("slorii X17 X17 12 3025")
    tran0.writeAction("slorii X17 X17 12 2087")
    tran0.writeAction("slorii X17 X17 12 2372")
    tran0.writeAction("slorii X17 X17 12 1429")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
