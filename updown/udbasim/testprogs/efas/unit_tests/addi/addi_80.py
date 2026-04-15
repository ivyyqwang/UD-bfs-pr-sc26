from EFA_v2 import *
def addi_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5714154071889717249, -26269]
    tran0.writeAction("movir X16 20300")
    tran0.writeAction("slorii X16 X16 12 3085")
    tran0.writeAction("slorii X16 X16 12 2686")
    tran0.writeAction("slorii X16 X16 12 3434")
    tran0.writeAction("slorii X16 X16 12 2049")
    tran0.writeAction("addi X16 X17 -26269")
    tran0.writeAction("yieldt")
    return efa
