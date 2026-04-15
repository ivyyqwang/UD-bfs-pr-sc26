from EFA_v2 import *
def srsubii_38():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4369566367595777056, 6, 1987]
    tran0.writeAction("movir X16 15523")
    tran0.writeAction("slorii X16 X16 12 3351")
    tran0.writeAction("slorii X16 X16 12 1499")
    tran0.writeAction("slorii X16 X16 12 164")
    tran0.writeAction("slorii X16 X16 12 3104")
    tran0.writeAction("srsubii X16 X17 6 1987")
    tran0.writeAction("yieldt")
    return efa
