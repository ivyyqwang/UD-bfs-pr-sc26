from EFA_v2 import *
def fsub_64_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5448681369070712563, 5929680747725595307]
    tran0.writeAction("movir X16 19357")
    tran0.writeAction("slorii X16 X16 12 2477")
    tran0.writeAction("slorii X16 X16 12 1593")
    tran0.writeAction("slorii X16 X16 12 3067")
    tran0.writeAction("slorii X16 X16 12 1779")
    tran0.writeAction("movir X17 21066")
    tran0.writeAction("slorii X17 X17 12 1875")
    tran0.writeAction("slorii X17 X17 12 2343")
    tran0.writeAction("slorii X17 X17 12 2690")
    tran0.writeAction("slorii X17 X17 12 683")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
