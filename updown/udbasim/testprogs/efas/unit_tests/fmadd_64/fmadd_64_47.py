from EFA_v2 import *
def fmadd_64_47():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8825089428739079096, 10366131574480172756, 5511754956629842473]
    tran0.writeAction("movir X16 31353")
    tran0.writeAction("slorii X16 X16 12 65")
    tran0.writeAction("slorii X16 X16 12 1023")
    tran0.writeAction("slorii X16 X16 12 195")
    tran0.writeAction("slorii X16 X16 12 3000")
    tran0.writeAction("movir X17 36827")
    tran0.writeAction("slorii X17 X17 12 3675")
    tran0.writeAction("slorii X17 X17 12 3759")
    tran0.writeAction("slorii X17 X17 12 3487")
    tran0.writeAction("slorii X17 X17 12 1748")
    tran0.writeAction("movir X18 19581")
    tran0.writeAction("slorii X18 X18 12 2814")
    tran0.writeAction("slorii X18 X18 12 3638")
    tran0.writeAction("slorii X18 X18 12 3769")
    tran0.writeAction("slorii X18 X18 12 2601")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
