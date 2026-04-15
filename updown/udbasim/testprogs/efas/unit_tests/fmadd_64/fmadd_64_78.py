from EFA_v2 import *
def fmadd_64_78():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12907304056097978688, 1806719876676852862, 11050545183587350849]
    tran0.writeAction("movir X16 45855")
    tran0.writeAction("slorii X16 X16 12 3914")
    tran0.writeAction("slorii X16 X16 12 1847")
    tran0.writeAction("slorii X16 X16 12 2779")
    tran0.writeAction("slorii X16 X16 12 2368")
    tran0.writeAction("movir X17 6418")
    tran0.writeAction("slorii X17 X17 12 3106")
    tran0.writeAction("slorii X17 X17 12 1993")
    tran0.writeAction("slorii X17 X17 12 3937")
    tran0.writeAction("slorii X17 X17 12 3198")
    tran0.writeAction("movir X18 39259")
    tran0.writeAction("slorii X18 X18 12 1732")
    tran0.writeAction("slorii X18 X18 12 3026")
    tran0.writeAction("slorii X18 X18 12 523")
    tran0.writeAction("slorii X18 X18 12 2369")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
