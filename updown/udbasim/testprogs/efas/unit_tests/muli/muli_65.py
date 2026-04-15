from EFA_v2 import *
def muli_65():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6046791429183253521, 27470]
    tran0.writeAction("movir X16 44053")
    tran0.writeAction("slorii X16 X16 12 1971")
    tran0.writeAction("slorii X16 X16 12 2944")
    tran0.writeAction("slorii X16 X16 12 2685")
    tran0.writeAction("slorii X16 X16 12 1007")
    tran0.writeAction("muli X16 X17 27470")
    tran0.writeAction("yieldt")
    return efa
