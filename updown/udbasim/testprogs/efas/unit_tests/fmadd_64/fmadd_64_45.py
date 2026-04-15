from EFA_v2 import *
def fmadd_64_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13971254346221333697, 1305738182612088210, 4854203404418329741]
    tran0.writeAction("movir X16 49635")
    tran0.writeAction("slorii X16 X16 12 3548")
    tran0.writeAction("slorii X16 X16 12 3605")
    tran0.writeAction("slorii X16 X16 12 634")
    tran0.writeAction("slorii X16 X16 12 3265")
    tran0.writeAction("movir X17 4638")
    tran0.writeAction("slorii X17 X17 12 3743")
    tran0.writeAction("slorii X17 X17 12 1408")
    tran0.writeAction("slorii X17 X17 12 1055")
    tran0.writeAction("slorii X17 X17 12 1426")
    tran0.writeAction("movir X18 17245")
    tran0.writeAction("slorii X18 X18 12 2436")
    tran0.writeAction("slorii X18 X18 12 1811")
    tran0.writeAction("slorii X18 X18 12 3466")
    tran0.writeAction("slorii X18 X18 12 3213")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
