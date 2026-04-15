from EFA_v2 import *
def fadd_64_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12321570969731296275, 5672434640888147801]
    tran0.writeAction("movir X16 43775")
    tran0.writeAction("slorii X16 X16 12 56")
    tran0.writeAction("slorii X16 X16 12 949")
    tran0.writeAction("slorii X16 X16 12 2454")
    tran0.writeAction("slorii X16 X16 12 3091")
    tran0.writeAction("movir X17 20152")
    tran0.writeAction("slorii X17 X17 12 2196")
    tran0.writeAction("slorii X17 X17 12 133")
    tran0.writeAction("slorii X17 X17 12 3106")
    tran0.writeAction("slorii X17 X17 12 3929")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
