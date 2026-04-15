from EFA_v2 import *
def fadd_64_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8407255116134454172, 8539151685230014329]
    tran0.writeAction("movir X16 29868")
    tran0.writeAction("slorii X16 X16 12 2335")
    tran0.writeAction("slorii X16 X16 12 3085")
    tran0.writeAction("slorii X16 X16 12 1145")
    tran0.writeAction("slorii X16 X16 12 924")
    tran0.writeAction("movir X17 30337")
    tran0.writeAction("slorii X17 X17 12 659")
    tran0.writeAction("slorii X17 X17 12 1825")
    tran0.writeAction("slorii X17 X17 12 1282")
    tran0.writeAction("slorii X17 X17 12 3961")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
