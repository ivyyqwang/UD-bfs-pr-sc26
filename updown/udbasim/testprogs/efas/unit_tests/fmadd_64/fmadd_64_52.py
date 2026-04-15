from EFA_v2 import *
def fmadd_64_52():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17535563282568314446, 3516606395244629132, 14436570560145347579]
    tran0.writeAction("movir X16 62298")
    tran0.writeAction("slorii X16 X16 12 3422")
    tran0.writeAction("slorii X16 X16 12 1513")
    tran0.writeAction("slorii X16 X16 12 3551")
    tran0.writeAction("slorii X16 X16 12 3662")
    tran0.writeAction("movir X17 12493")
    tran0.writeAction("slorii X17 X17 12 2030")
    tran0.writeAction("slorii X17 X17 12 635")
    tran0.writeAction("slorii X17 X17 12 1732")
    tran0.writeAction("slorii X17 X17 12 3212")
    tran0.writeAction("movir X18 51289")
    tran0.writeAction("slorii X18 X18 12 6")
    tran0.writeAction("slorii X18 X18 12 4012")
    tran0.writeAction("slorii X18 X18 12 1333")
    tran0.writeAction("slorii X18 X18 12 1019")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
