from EFA_v2 import *
def srsubii_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7601736831127107321, 1, 703]
    tran0.writeAction("movir X16 38529")
    tran0.writeAction("slorii X16 X16 12 842")
    tran0.writeAction("slorii X16 X16 12 184")
    tran0.writeAction("slorii X16 X16 12 2724")
    tran0.writeAction("slorii X16 X16 12 2311")
    tran0.writeAction("srsubii X16 X17 1 703")
    tran0.writeAction("yieldt")
    return efa
