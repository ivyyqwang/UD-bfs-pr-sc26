from EFA_v2 import *
def mul_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6617721501078061213, 7184176956429968795]
    tran0.writeAction("movir X16 42025")
    tran0.writeAction("slorii X16 X16 12 533")
    tran0.writeAction("slorii X16 X16 12 2913")
    tran0.writeAction("slorii X16 X16 12 3183")
    tran0.writeAction("slorii X16 X16 12 3939")
    tran0.writeAction("movir X17 25523")
    tran0.writeAction("slorii X17 X17 12 1326")
    tran0.writeAction("slorii X17 X17 12 227")
    tran0.writeAction("slorii X17 X17 12 2274")
    tran0.writeAction("slorii X17 X17 12 1435")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
