from EFA_v2 import *
def div_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4043222508825594788, 2825444294065655199]
    tran0.writeAction("movir X16 51171")
    tran0.writeAction("slorii X16 X16 12 2408")
    tran0.writeAction("slorii X16 X16 12 3285")
    tran0.writeAction("slorii X16 X16 12 2403")
    tran0.writeAction("slorii X16 X16 12 1116")
    tran0.writeAction("movir X17 10037")
    tran0.writeAction("slorii X17 X17 12 4073")
    tran0.writeAction("slorii X17 X17 12 3480")
    tran0.writeAction("slorii X17 X17 12 1792")
    tran0.writeAction("slorii X17 X17 12 3487")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
