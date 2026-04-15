from EFA_v2 import *
def srsubii_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7112401153978861475, 4, 1849]
    tran0.writeAction("movir X16 25268")
    tran0.writeAction("slorii X16 X16 12 1330")
    tran0.writeAction("slorii X16 X16 12 2714")
    tran0.writeAction("slorii X16 X16 12 4048")
    tran0.writeAction("slorii X16 X16 12 1955")
    tran0.writeAction("srsubii X16 X17 4 1849")
    tran0.writeAction("yieldt")
    return efa
