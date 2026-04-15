from EFA_v2 import *
def srsubii_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1171541363300233057, 10, 1185]
    tran0.writeAction("movir X16 4162")
    tran0.writeAction("slorii X16 X16 12 618")
    tran0.writeAction("slorii X16 X16 12 2479")
    tran0.writeAction("slorii X16 X16 12 766")
    tran0.writeAction("slorii X16 X16 12 3937")
    tran0.writeAction("srsubii X16 X17 10 1185")
    tran0.writeAction("yieldt")
    return efa
