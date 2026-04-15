from EFA_v2 import *
def fadd_64_92():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2534125157138847504, 10823939586819894349]
    tran0.writeAction("movir X16 9003")
    tran0.writeAction("slorii X16 X16 12 86")
    tran0.writeAction("slorii X16 X16 12 1903")
    tran0.writeAction("slorii X16 X16 12 2629")
    tran0.writeAction("slorii X16 X16 12 1808")
    tran0.writeAction("movir X17 38454")
    tran0.writeAction("slorii X17 X17 12 1467")
    tran0.writeAction("slorii X17 X17 12 1246")
    tran0.writeAction("slorii X17 X17 12 2818")
    tran0.writeAction("slorii X17 X17 12 3149")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
