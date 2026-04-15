from EFA_v2 import *
def fmul_64_44():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [434723404155222348, 14849085750934674391]
    tran0.writeAction("movir X16 1544")
    tran0.writeAction("slorii X16 X16 12 1834")
    tran0.writeAction("slorii X16 X16 12 512")
    tran0.writeAction("slorii X16 X16 12 903")
    tran0.writeAction("slorii X16 X16 12 2380")
    tran0.writeAction("movir X17 52754")
    tran0.writeAction("slorii X17 X17 12 2253")
    tran0.writeAction("slorii X17 X17 12 271")
    tran0.writeAction("slorii X17 X17 12 3177")
    tran0.writeAction("slorii X17 X17 12 3031")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
