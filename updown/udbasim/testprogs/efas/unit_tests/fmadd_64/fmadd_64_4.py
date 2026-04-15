from EFA_v2 import *
def fmadd_64_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16713371604870479780, 12724400270202242510, 2946301266763598086]
    tran0.writeAction("movir X16 59377")
    tran0.writeAction("slorii X16 X16 12 3374")
    tran0.writeAction("slorii X16 X16 12 3171")
    tran0.writeAction("slorii X16 X16 12 1659")
    tran0.writeAction("slorii X16 X16 12 4004")
    tran0.writeAction("movir X17 45206")
    tran0.writeAction("slorii X17 X17 12 618")
    tran0.writeAction("slorii X17 X17 12 261")
    tran0.writeAction("slorii X17 X17 12 1184")
    tran0.writeAction("slorii X17 X17 12 1486")
    tran0.writeAction("movir X18 10467")
    tran0.writeAction("slorii X18 X18 12 1494")
    tran0.writeAction("slorii X18 X18 12 1110")
    tran0.writeAction("slorii X18 X18 12 2980")
    tran0.writeAction("slorii X18 X18 12 2310")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
