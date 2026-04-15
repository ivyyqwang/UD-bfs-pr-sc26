from EFA_v2 import *
def fsub_64_36():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12204015480024917424, 740943619318527195]
    tran0.writeAction("movir X16 43357")
    tran0.writeAction("slorii X16 X16 12 1526")
    tran0.writeAction("slorii X16 X16 12 2912")
    tran0.writeAction("slorii X16 X16 12 1038")
    tran0.writeAction("slorii X16 X16 12 1456")
    tran0.writeAction("movir X17 2632")
    tran0.writeAction("slorii X17 X17 12 1476")
    tran0.writeAction("slorii X17 X17 12 3020")
    tran0.writeAction("slorii X17 X17 12 299")
    tran0.writeAction("slorii X17 X17 12 1243")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
