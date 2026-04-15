from EFA_v2 import *
def fmadd_32_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [701877676, 346877656, 2622890639]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 41")
    tran0.writeAction("slorii X16 X16 12 3420")
    tran0.writeAction("slorii X16 X16 12 3500")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 20")
    tran0.writeAction("slorii X17 X17 12 2766")
    tran0.writeAction("slorii X17 X17 12 3800")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 156")
    tran0.writeAction("slorii X18 X18 12 1378")
    tran0.writeAction("slorii X18 X18 12 655")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
