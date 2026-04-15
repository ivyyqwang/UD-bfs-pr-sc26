from EFA_v2 import *
def fmadd_64_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15737101598929744268, 7507779315830916991, 11016331905641509401]
    tran0.writeAction("movir X16 55909")
    tran0.writeAction("slorii X16 X16 12 1704")
    tran0.writeAction("slorii X16 X16 12 1670")
    tran0.writeAction("slorii X16 X16 12 1799")
    tran0.writeAction("slorii X16 X16 12 396")
    tran0.writeAction("movir X17 26672")
    tran0.writeAction("slorii X17 X17 12 4056")
    tran0.writeAction("slorii X17 X17 12 644")
    tran0.writeAction("slorii X17 X17 12 520")
    tran0.writeAction("slorii X17 X17 12 1919")
    tran0.writeAction("movir X18 39137")
    tran0.writeAction("slorii X18 X18 12 3576")
    tran0.writeAction("slorii X18 X18 12 75")
    tran0.writeAction("slorii X18 X18 12 2311")
    tran0.writeAction("slorii X18 X18 12 537")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
