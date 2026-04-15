from EFA_v2 import *
def sladdii_82():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-9025222959247932422, 4, 450]
    tran0.writeAction("movir X16 33471")
    tran0.writeAction("slorii X16 X16 12 3960")
    tran0.writeAction("slorii X16 X16 12 2375")
    tran0.writeAction("slorii X16 X16 12 1340")
    tran0.writeAction("slorii X16 X16 12 1018")
    tran0.writeAction("sladdii X16 X17 4 450")
    tran0.writeAction("yieldt")
    return efa
