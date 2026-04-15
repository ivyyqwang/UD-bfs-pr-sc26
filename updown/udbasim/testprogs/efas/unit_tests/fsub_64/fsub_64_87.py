from EFA_v2 import *
def fsub_64_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12314619299802972732, 757924123908322421]
    tran0.writeAction("movir X16 43750")
    tran0.writeAction("slorii X16 X16 12 1296")
    tran0.writeAction("slorii X16 X16 12 492")
    tran0.writeAction("slorii X16 X16 12 3792")
    tran0.writeAction("slorii X16 X16 12 572")
    tran0.writeAction("movir X17 2692")
    tran0.writeAction("slorii X17 X17 12 2815")
    tran0.writeAction("slorii X17 X17 12 2460")
    tran0.writeAction("slorii X17 X17 12 1043")
    tran0.writeAction("slorii X17 X17 12 1141")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
