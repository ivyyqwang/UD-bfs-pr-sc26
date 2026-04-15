from EFA_v2 import *
def fdiv_64_60():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2729056449323709723, 8689873035989208175]
    tran0.writeAction("movir X16 9695")
    tran0.writeAction("slorii X16 X16 12 2278")
    tran0.writeAction("slorii X16 X16 12 425")
    tran0.writeAction("slorii X16 X16 12 3803")
    tran0.writeAction("slorii X16 X16 12 1307")
    tran0.writeAction("movir X17 30872")
    tran0.writeAction("slorii X17 X17 12 2583")
    tran0.writeAction("slorii X17 X17 12 3133")
    tran0.writeAction("slorii X17 X17 12 1564")
    tran0.writeAction("slorii X17 X17 12 3183")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
