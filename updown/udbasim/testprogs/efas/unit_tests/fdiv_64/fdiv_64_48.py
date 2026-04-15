from EFA_v2 import *
def fdiv_64_48():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8129203798825876915, 10475824973309199225]
    tran0.writeAction("movir X16 28880")
    tran0.writeAction("slorii X16 X16 12 3004")
    tran0.writeAction("slorii X16 X16 12 2271")
    tran0.writeAction("slorii X16 X16 12 3163")
    tran0.writeAction("slorii X16 X16 12 3507")
    tran0.writeAction("movir X17 37217")
    tran0.writeAction("slorii X17 X17 12 2484")
    tran0.writeAction("slorii X17 X17 12 3927")
    tran0.writeAction("slorii X17 X17 12 1068")
    tran0.writeAction("slorii X17 X17 12 889")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
