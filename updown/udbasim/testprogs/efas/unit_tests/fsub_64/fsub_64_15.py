from EFA_v2 import *
def fsub_64_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1944833221122310478, 1939381640254783611]
    tran0.writeAction("movir X16 6909")
    tran0.writeAction("slorii X16 X16 12 1784")
    tran0.writeAction("slorii X16 X16 12 684")
    tran0.writeAction("slorii X16 X16 12 1532")
    tran0.writeAction("slorii X16 X16 12 334")
    tran0.writeAction("movir X17 6890")
    tran0.writeAction("slorii X17 X17 12 277")
    tran0.writeAction("slorii X17 X17 12 919")
    tran0.writeAction("slorii X17 X17 12 1232")
    tran0.writeAction("slorii X17 X17 12 123")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
