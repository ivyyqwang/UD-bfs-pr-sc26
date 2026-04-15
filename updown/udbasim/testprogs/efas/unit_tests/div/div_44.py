from EFA_v2 import *
def div_44():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [484342759098907719, -7342283905607046994]
    tran0.writeAction("movir X16 1720")
    tran0.writeAction("slorii X16 X16 12 2994")
    tran0.writeAction("slorii X16 X16 12 3161")
    tran0.writeAction("slorii X16 X16 12 2551")
    tran0.writeAction("slorii X16 X16 12 3143")
    tran0.writeAction("movir X17 39450")
    tran0.writeAction("slorii X17 X17 12 3963")
    tran0.writeAction("slorii X17 X17 12 94")
    tran0.writeAction("slorii X17 X17 12 918")
    tran0.writeAction("slorii X17 X17 12 2222")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
