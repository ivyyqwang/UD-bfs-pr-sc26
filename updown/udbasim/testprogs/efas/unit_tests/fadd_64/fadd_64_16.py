from EFA_v2 import *
def fadd_64_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10002373688436116815, 11557000000045464112]
    tran0.writeAction("movir X16 35535")
    tran0.writeAction("slorii X16 X16 12 2333")
    tran0.writeAction("slorii X16 X16 12 4081")
    tran0.writeAction("slorii X16 X16 12 3884")
    tran0.writeAction("slorii X16 X16 12 3407")
    tran0.writeAction("movir X17 41058")
    tran0.writeAction("slorii X17 X17 12 2916")
    tran0.writeAction("slorii X17 X17 12 1207")
    tran0.writeAction("slorii X17 X17 12 3683")
    tran0.writeAction("slorii X17 X17 12 2608")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
