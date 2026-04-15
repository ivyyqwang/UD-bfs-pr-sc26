from EFA_v2 import *
def fmadd_64_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17593248068871652800, 1986295819162972708, 15803587545533372298]
    tran0.writeAction("movir X16 62503")
    tran0.writeAction("slorii X16 X16 12 3166")
    tran0.writeAction("slorii X16 X16 12 2006")
    tran0.writeAction("slorii X16 X16 12 1728")
    tran0.writeAction("slorii X16 X16 12 1472")
    tran0.writeAction("movir X17 7056")
    tran0.writeAction("slorii X17 X17 12 3032")
    tran0.writeAction("slorii X17 X17 12 1552")
    tran0.writeAction("slorii X17 X17 12 215")
    tran0.writeAction("slorii X17 X17 12 548")
    tran0.writeAction("movir X18 56145")
    tran0.writeAction("slorii X18 X18 12 2546")
    tran0.writeAction("slorii X18 X18 12 1092")
    tran0.writeAction("slorii X18 X18 12 1245")
    tran0.writeAction("slorii X18 X18 12 1930")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
