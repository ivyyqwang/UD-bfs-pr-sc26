from EFA_v2 import *
def fmul_64_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9295940012227462595, 2918865763166409178]
    tran0.writeAction("movir X16 33025")
    tran0.writeAction("slorii X16 X16 12 3331")
    tran0.writeAction("slorii X16 X16 12 106")
    tran0.writeAction("slorii X16 X16 12 648")
    tran0.writeAction("slorii X16 X16 12 1475")
    tran0.writeAction("movir X17 10369")
    tran0.writeAction("slorii X17 X17 12 3663")
    tran0.writeAction("slorii X17 X17 12 608")
    tran0.writeAction("slorii X17 X17 12 2389")
    tran0.writeAction("slorii X17 X17 12 474")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
