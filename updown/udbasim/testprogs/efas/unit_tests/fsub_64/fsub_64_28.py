from EFA_v2 import *
def fsub_64_28():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [287539418780346740, 5008985325842572345]
    tran0.writeAction("movir X16 1021")
    tran0.writeAction("slorii X16 X16 12 2233")
    tran0.writeAction("slorii X16 X16 12 1011")
    tran0.writeAction("slorii X16 X16 12 1330")
    tran0.writeAction("slorii X16 X16 12 2420")
    tran0.writeAction("movir X17 17795")
    tran0.writeAction("slorii X17 X17 12 2009")
    tran0.writeAction("slorii X17 X17 12 3447")
    tran0.writeAction("slorii X17 X17 12 4058")
    tran0.writeAction("slorii X17 X17 12 1081")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
