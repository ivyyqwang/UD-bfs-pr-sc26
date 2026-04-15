from EFA_v2 import *
def fmadd_64_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7113469046936892254, 555971180305625569, 12636183922559509127]
    tran0.writeAction("movir X16 25272")
    tran0.writeAction("slorii X16 X16 12 486")
    tran0.writeAction("slorii X16 X16 12 2255")
    tran0.writeAction("slorii X16 X16 12 1679")
    tran0.writeAction("slorii X16 X16 12 862")
    tran0.writeAction("movir X17 1975")
    tran0.writeAction("slorii X17 X17 12 845")
    tran0.writeAction("slorii X17 X17 12 1987")
    tran0.writeAction("slorii X17 X17 12 1931")
    tran0.writeAction("slorii X17 X17 12 481")
    tran0.writeAction("movir X18 44892")
    tran0.writeAction("slorii X18 X18 12 3045")
    tran0.writeAction("slorii X18 X18 12 1028")
    tran0.writeAction("slorii X18 X18 12 2710")
    tran0.writeAction("slorii X18 X18 12 647")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
