from EFA_v2 import *
def fsub_64_54():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6588438657528454122, 7403518251647067363]
    tran0.writeAction("movir X16 23406")
    tran0.writeAction("slorii X16 X16 12 3424")
    tran0.writeAction("slorii X16 X16 12 3406")
    tran0.writeAction("slorii X16 X16 12 1781")
    tran0.writeAction("slorii X16 X16 12 3050")
    tran0.writeAction("movir X17 26302")
    tran0.writeAction("slorii X17 X17 12 2377")
    tran0.writeAction("slorii X17 X17 12 4053")
    tran0.writeAction("slorii X17 X17 12 2230")
    tran0.writeAction("slorii X17 X17 12 1251")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
