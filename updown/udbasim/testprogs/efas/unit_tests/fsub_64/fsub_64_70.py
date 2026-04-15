from EFA_v2 import *
def fsub_64_70():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5684094356851008353, 16477853838809766657]
    tran0.writeAction("movir X16 20193")
    tran0.writeAction("slorii X16 X16 12 3931")
    tran0.writeAction("slorii X16 X16 12 945")
    tran0.writeAction("slorii X16 X16 12 3714")
    tran0.writeAction("slorii X16 X16 12 865")
    tran0.writeAction("movir X17 58541")
    tran0.writeAction("slorii X17 X17 12 396")
    tran0.writeAction("slorii X17 X17 12 851")
    tran0.writeAction("slorii X17 X17 12 257")
    tran0.writeAction("slorii X17 X17 12 2817")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
