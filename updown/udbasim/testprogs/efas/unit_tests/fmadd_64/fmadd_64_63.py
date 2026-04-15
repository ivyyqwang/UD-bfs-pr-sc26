from EFA_v2 import *
def fmadd_64_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18396786539749816008, 10175739647870072225, 15033345959713393199]
    tran0.writeAction("movir X16 65358")
    tran0.writeAction("slorii X16 X16 12 2110")
    tran0.writeAction("slorii X16 X16 12 822")
    tran0.writeAction("slorii X16 X16 12 1947")
    tran0.writeAction("slorii X16 X16 12 1736")
    tran0.writeAction("movir X17 36151")
    tran0.writeAction("slorii X17 X17 12 2004")
    tran0.writeAction("slorii X17 X17 12 3038")
    tran0.writeAction("slorii X17 X17 12 631")
    tran0.writeAction("slorii X17 X17 12 1441")
    tran0.writeAction("movir X18 53409")
    tran0.writeAction("slorii X18 X18 12 712")
    tran0.writeAction("slorii X18 X18 12 18")
    tran0.writeAction("slorii X18 X18 12 1108")
    tran0.writeAction("slorii X18 X18 12 2607")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
