from EFA_v2 import *
def fdiv_64_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2482850139188648219, 9833061729958756076]
    tran0.writeAction("movir X16 8820")
    tran0.writeAction("slorii X16 X16 12 3504")
    tran0.writeAction("slorii X16 X16 12 3072")
    tran0.writeAction("slorii X16 X16 12 3557")
    tran0.writeAction("slorii X16 X16 12 2331")
    tran0.writeAction("movir X17 34934")
    tran0.writeAction("slorii X17 X17 12 216")
    tran0.writeAction("slorii X17 X17 12 2988")
    tran0.writeAction("slorii X17 X17 12 2783")
    tran0.writeAction("slorii X17 X17 12 3820")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
