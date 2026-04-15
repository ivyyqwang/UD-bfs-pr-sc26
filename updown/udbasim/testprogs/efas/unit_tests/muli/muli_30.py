from EFA_v2 import *
def muli_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1102149389513232952, 15117]
    tran0.writeAction("movir X16 3915")
    tran0.writeAction("slorii X16 X16 12 2544")
    tran0.writeAction("slorii X16 X16 12 1987")
    tran0.writeAction("slorii X16 X16 12 1433")
    tran0.writeAction("slorii X16 X16 12 568")
    tran0.writeAction("muli X16 X17 15117")
    tran0.writeAction("yieldt")
    return efa
