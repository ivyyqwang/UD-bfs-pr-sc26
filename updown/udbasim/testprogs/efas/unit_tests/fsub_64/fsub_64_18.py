from EFA_v2 import *
def fsub_64_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4993477606780785911, 14325089129982287255]
    tran0.writeAction("movir X16 17740")
    tran0.writeAction("slorii X16 X16 12 1622")
    tran0.writeAction("slorii X16 X16 12 3394")
    tran0.writeAction("slorii X16 X16 12 149")
    tran0.writeAction("slorii X16 X16 12 1271")
    tran0.writeAction("movir X17 50892")
    tran0.writeAction("slorii X17 X17 12 3850")
    tran0.writeAction("slorii X17 X17 12 2696")
    tran0.writeAction("slorii X17 X17 12 1653")
    tran0.writeAction("slorii X17 X17 12 3479")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
