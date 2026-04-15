from EFA_v2 import *
def hash_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5198486126406618580, 6274679674184285313]
    tran0.writeAction("movir X16 18468")
    tran0.writeAction("slorii X16 X16 12 3001")
    tran0.writeAction("slorii X16 X16 12 1750")
    tran0.writeAction("slorii X16 X16 12 1076")
    tran0.writeAction("slorii X16 X16 12 3540")
    tran0.writeAction("movir X17 22292")
    tran0.writeAction("slorii X17 X17 12 574")
    tran0.writeAction("slorii X17 X17 12 2883")
    tran0.writeAction("slorii X17 X17 12 483")
    tran0.writeAction("slorii X17 X17 12 3201")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
