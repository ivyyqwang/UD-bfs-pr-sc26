from EFA_v2 import *
def srsubii_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-34105079416955772, 2, 125]
    tran0.writeAction("movir X16 65414")
    tran0.writeAction("slorii X16 X16 12 3417")
    tran0.writeAction("slorii X16 X16 12 3176")
    tran0.writeAction("slorii X16 X16 12 1293")
    tran0.writeAction("slorii X16 X16 12 3204")
    tran0.writeAction("srsubii X16 X17 2 125")
    tran0.writeAction("yieldt")
    return efa
