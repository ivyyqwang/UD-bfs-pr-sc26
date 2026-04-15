from EFA_v2 import *
def fmadd_64_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [388756019770019361, 7798488954112119800, 11380922717827663781]
    tran0.writeAction("movir X16 1381")
    tran0.writeAction("slorii X16 X16 12 568")
    tran0.writeAction("slorii X16 X16 12 2638")
    tran0.writeAction("slorii X16 X16 12 2812")
    tran0.writeAction("slorii X16 X16 12 3617")
    tran0.writeAction("movir X17 27705")
    tran0.writeAction("slorii X17 X17 12 3270")
    tran0.writeAction("slorii X17 X17 12 694")
    tran0.writeAction("slorii X17 X17 12 2705")
    tran0.writeAction("slorii X17 X17 12 1016")
    tran0.writeAction("movir X18 40433")
    tran0.writeAction("slorii X18 X18 12 654")
    tran0.writeAction("slorii X18 X18 12 2500")
    tran0.writeAction("slorii X18 X18 12 1192")
    tran0.writeAction("slorii X18 X18 12 1957")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
