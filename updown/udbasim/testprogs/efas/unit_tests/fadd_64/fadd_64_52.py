from EFA_v2 import *
def fadd_64_52():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8824900307948236497, 16278472197045804098]
    tran0.writeAction("movir X16 31352")
    tran0.writeAction("slorii X16 X16 12 1409")
    tran0.writeAction("slorii X16 X16 12 737")
    tran0.writeAction("slorii X16 X16 12 2006")
    tran0.writeAction("slorii X16 X16 12 3793")
    tran0.writeAction("movir X17 57832")
    tran0.writeAction("slorii X17 X17 12 3075")
    tran0.writeAction("slorii X17 X17 12 1878")
    tran0.writeAction("slorii X17 X17 12 4045")
    tran0.writeAction("slorii X17 X17 12 3138")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
