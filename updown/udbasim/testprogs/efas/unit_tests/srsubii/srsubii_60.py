from EFA_v2 import *
def srsubii_60():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5096431379432935647, 2, 892]
    tran0.writeAction("movir X16 47429")
    tran0.writeAction("slorii X16 X16 12 3434")
    tran0.writeAction("slorii X16 X16 12 2454")
    tran0.writeAction("slorii X16 X16 12 3054")
    tran0.writeAction("slorii X16 X16 12 3873")
    tran0.writeAction("srsubii X16 X17 2 892")
    tran0.writeAction("yieldt")
    return efa
