from EFA_v2 import *
def fmadd_64_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8316243477694781444, 11559083501118146928, 4026303990090833671]
    tran0.writeAction("movir X16 29545")
    tran0.writeAction("slorii X16 X16 12 950")
    tran0.writeAction("slorii X16 X16 12 433")
    tran0.writeAction("slorii X16 X16 12 2689")
    tran0.writeAction("slorii X16 X16 12 2052")
    tran0.writeAction("movir X17 41066")
    tran0.writeAction("slorii X17 X17 12 467")
    tran0.writeAction("slorii X17 X17 12 925")
    tran0.writeAction("slorii X17 X17 12 924")
    tran0.writeAction("slorii X17 X17 12 2416")
    tran0.writeAction("movir X18 14304")
    tran0.writeAction("slorii X18 X18 12 1250")
    tran0.writeAction("slorii X18 X18 12 1423")
    tran0.writeAction("slorii X18 X18 12 417")
    tran0.writeAction("slorii X18 X18 12 3847")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
