from EFA_v2 import *
def sladdii_32():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5421066694849809147, 11, 288]
    tran0.writeAction("movir X16 19259")
    tran0.writeAction("slorii X16 X16 12 2038")
    tran0.writeAction("slorii X16 X16 12 4058")
    tran0.writeAction("slorii X16 X16 12 916")
    tran0.writeAction("slorii X16 X16 12 2811")
    tran0.writeAction("sladdii X16 X17 11 288")
    tran0.writeAction("yieldt")
    return efa
