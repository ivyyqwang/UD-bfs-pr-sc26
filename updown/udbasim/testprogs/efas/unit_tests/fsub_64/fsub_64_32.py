from EFA_v2 import *
def fsub_64_32():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [606716711310036051, 5399783837666572325]
    tran0.writeAction("movir X16 2155")
    tran0.writeAction("slorii X16 X16 12 2010")
    tran0.writeAction("slorii X16 X16 12 616")
    tran0.writeAction("slorii X16 X16 12 3800")
    tran0.writeAction("slorii X16 X16 12 3155")
    tran0.writeAction("movir X17 19183")
    tran0.writeAction("slorii X17 X17 12 3628")
    tran0.writeAction("slorii X17 X17 12 2692")
    tran0.writeAction("slorii X17 X17 12 47")
    tran0.writeAction("slorii X17 X17 12 2085")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
