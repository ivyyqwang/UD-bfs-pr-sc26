from EFA_v2 import *
def fadd_64_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14807347513559617845, 4092753790229140087]
    tran0.writeAction("movir X16 52606")
    tran0.writeAction("slorii X16 X16 12 1089")
    tran0.writeAction("slorii X16 X16 12 3171")
    tran0.writeAction("slorii X16 X16 12 1985")
    tran0.writeAction("slorii X16 X16 12 309")
    tran0.writeAction("movir X17 14540")
    tran0.writeAction("slorii X17 X17 12 1566")
    tran0.writeAction("slorii X17 X17 12 843")
    tran0.writeAction("slorii X17 X17 12 3037")
    tran0.writeAction("slorii X17 X17 12 631")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
