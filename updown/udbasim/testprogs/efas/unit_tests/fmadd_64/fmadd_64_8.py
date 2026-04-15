from EFA_v2 import *
def fmadd_64_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8512188976068068655, 18393915430248669779, 1750816840177943990]
    tran0.writeAction("movir X16 30241")
    tran0.writeAction("slorii X16 X16 12 1516")
    tran0.writeAction("slorii X16 X16 12 1587")
    tran0.writeAction("slorii X16 X16 12 2184")
    tran0.writeAction("slorii X16 X16 12 1327")
    tran0.writeAction("movir X17 65348")
    tran0.writeAction("slorii X17 X17 12 1290")
    tran0.writeAction("slorii X17 X17 12 240")
    tran0.writeAction("slorii X17 X17 12 2246")
    tran0.writeAction("slorii X17 X17 12 595")
    tran0.writeAction("movir X18 6220")
    tran0.writeAction("slorii X18 X18 12 618")
    tran0.writeAction("slorii X18 X18 12 977")
    tran0.writeAction("slorii X18 X18 12 2368")
    tran0.writeAction("slorii X18 X18 12 1462")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
