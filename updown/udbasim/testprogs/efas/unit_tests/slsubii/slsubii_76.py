from EFA_v2 import *
def slsubii_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2276786572572078292, 8, 1193]
    tran0.writeAction("movir X16 8088")
    tran0.writeAction("slorii X16 X16 12 3157")
    tran0.writeAction("slorii X16 X16 12 807")
    tran0.writeAction("slorii X16 X16 12 2203")
    tran0.writeAction("slorii X16 X16 12 212")
    tran0.writeAction("slsubii X16 X17 8 1193")
    tran0.writeAction("yieldt")
    return efa
