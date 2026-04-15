from EFA_v2 import *
def sladdii_38():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5822186182145852725, 2, 82]
    tran0.writeAction("movir X16 44851")
    tran0.writeAction("slorii X16 X16 12 1800")
    tran0.writeAction("slorii X16 X16 12 957")
    tran0.writeAction("slorii X16 X16 12 35")
    tran0.writeAction("slorii X16 X16 12 2763")
    tran0.writeAction("sladdii X16 X17 2 82")
    tran0.writeAction("yieldt")
    return efa
