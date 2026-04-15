from EFA_v2 import *
def srsubii_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1777546800003334734, 13, 639]
    tran0.writeAction("movir X16 6315")
    tran0.writeAction("slorii X16 X16 12 470")
    tran0.writeAction("slorii X16 X16 12 1425")
    tran0.writeAction("slorii X16 X16 12 3404")
    tran0.writeAction("slorii X16 X16 12 590")
    tran0.writeAction("srsubii X16 X17 13 639")
    tran0.writeAction("yieldt")
    return efa
