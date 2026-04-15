from EFA_v2 import *
def fsub_64_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7381348393870689013, 15056315869985948452]
    tran0.writeAction("movir X16 26223")
    tran0.writeAction("slorii X16 X16 12 3348")
    tran0.writeAction("slorii X16 X16 12 404")
    tran0.writeAction("slorii X16 X16 12 256")
    tran0.writeAction("slorii X16 X16 12 757")
    tran0.writeAction("movir X17 53490")
    tran0.writeAction("slorii X17 X17 12 3192")
    tran0.writeAction("slorii X17 X17 12 784")
    tran0.writeAction("slorii X17 X17 12 2412")
    tran0.writeAction("slorii X17 X17 12 804")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
