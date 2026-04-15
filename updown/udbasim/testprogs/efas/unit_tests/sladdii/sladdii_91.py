from EFA_v2 import *
def sladdii_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7958435216655504453, 5, 1761]
    tran0.writeAction("movir X16 37261")
    tran0.writeAction("slorii X16 X16 12 3925")
    tran0.writeAction("slorii X16 X16 12 1543")
    tran0.writeAction("slorii X16 X16 12 1186")
    tran0.writeAction("slorii X16 X16 12 3003")
    tran0.writeAction("sladdii X16 X17 5 1761")
    tran0.writeAction("yieldt")
    return efa
