from EFA_v2 import *
def fsub_64_83():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8903824746136207692, 6480297894954399058]
    tran0.writeAction("movir X16 31632")
    tran0.writeAction("slorii X16 X16 12 3030")
    tran0.writeAction("slorii X16 X16 12 3743")
    tran0.writeAction("slorii X16 X16 12 3200")
    tran0.writeAction("slorii X16 X16 12 332")
    tran0.writeAction("movir X17 23022")
    tran0.writeAction("slorii X17 X17 12 2633")
    tran0.writeAction("slorii X17 X17 12 2547")
    tran0.writeAction("slorii X17 X17 12 1919")
    tran0.writeAction("slorii X17 X17 12 1362")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
