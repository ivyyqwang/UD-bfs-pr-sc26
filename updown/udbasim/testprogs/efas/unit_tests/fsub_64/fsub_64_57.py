from EFA_v2 import *
def fsub_64_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12513104702282959549, 11539146923138500500]
    tran0.writeAction("movir X16 44455")
    tran0.writeAction("slorii X16 X16 12 1958")
    tran0.writeAction("slorii X16 X16 12 3568")
    tran0.writeAction("slorii X16 X16 12 3464")
    tran0.writeAction("slorii X16 X16 12 2749")
    tran0.writeAction("movir X17 40995")
    tran0.writeAction("slorii X17 X17 12 1167")
    tran0.writeAction("slorii X17 X17 12 3412")
    tran0.writeAction("slorii X17 X17 12 2916")
    tran0.writeAction("slorii X17 X17 12 1940")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
