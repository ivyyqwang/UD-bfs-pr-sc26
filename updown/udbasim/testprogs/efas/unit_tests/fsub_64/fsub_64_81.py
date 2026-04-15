from EFA_v2 import *
def fsub_64_81():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18408903671744772687, 14706080623148646277]
    tran0.writeAction("movir X16 65401")
    tran0.writeAction("slorii X16 X16 12 2309")
    tran0.writeAction("slorii X16 X16 12 2778")
    tran0.writeAction("slorii X16 X16 12 2995")
    tran0.writeAction("slorii X16 X16 12 2639")
    tran0.writeAction("movir X17 52246")
    tran0.writeAction("slorii X17 X17 12 2022")
    tran0.writeAction("slorii X17 X17 12 2333")
    tran0.writeAction("slorii X17 X17 12 123")
    tran0.writeAction("slorii X17 X17 12 3973")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
