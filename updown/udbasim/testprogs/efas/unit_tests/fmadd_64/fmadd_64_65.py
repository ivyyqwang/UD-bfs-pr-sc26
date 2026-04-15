from EFA_v2 import *
def fmadd_64_65():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13658134723743781556, 223700421061600842, 15026360106383004482]
    tran0.writeAction("movir X16 48523")
    tran0.writeAction("slorii X16 X16 12 1810")
    tran0.writeAction("slorii X16 X16 12 2775")
    tran0.writeAction("slorii X16 X16 12 721")
    tran0.writeAction("slorii X16 X16 12 692")
    tran0.writeAction("movir X17 794")
    tran0.writeAction("slorii X17 X17 12 3045")
    tran0.writeAction("slorii X17 X17 12 2309")
    tran0.writeAction("slorii X17 X17 12 1974")
    tran0.writeAction("slorii X17 X17 12 1610")
    tran0.writeAction("movir X18 53384")
    tran0.writeAction("slorii X18 X18 12 1454")
    tran0.writeAction("slorii X18 X18 12 1880")
    tran0.writeAction("slorii X18 X18 12 245")
    tran0.writeAction("slorii X18 X18 12 834")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
