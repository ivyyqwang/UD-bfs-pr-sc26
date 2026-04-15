from EFA_v2 import *
def fmadd_64_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2683317092291026652, 12465895957576667207, 8082406416527965998]
    tran0.writeAction("movir X16 9533")
    tran0.writeAction("slorii X16 X16 12 234")
    tran0.writeAction("slorii X16 X16 12 3513")
    tran0.writeAction("slorii X16 X16 12 3033")
    tran0.writeAction("slorii X16 X16 12 3804")
    tran0.writeAction("movir X17 44287")
    tran0.writeAction("slorii X17 X17 12 3109")
    tran0.writeAction("slorii X17 X17 12 902")
    tran0.writeAction("slorii X17 X17 12 1373")
    tran0.writeAction("slorii X17 X17 12 71")
    tran0.writeAction("movir X18 28714")
    tran0.writeAction("slorii X18 X18 12 1949")
    tran0.writeAction("slorii X18 X18 12 59")
    tran0.writeAction("slorii X18 X18 12 1995")
    tran0.writeAction("slorii X18 X18 12 3886")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
