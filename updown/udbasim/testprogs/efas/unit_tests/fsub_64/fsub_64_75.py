from EFA_v2 import *
def fsub_64_75():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5707233105431967210, 5851226142653895502]
    tran0.writeAction("movir X16 20276")
    tran0.writeAction("slorii X16 X16 12 676")
    tran0.writeAction("slorii X16 X16 12 1387")
    tran0.writeAction("slorii X16 X16 12 2547")
    tran0.writeAction("slorii X16 X16 12 1514")
    tran0.writeAction("movir X17 20787")
    tran0.writeAction("slorii X17 X17 12 2994")
    tran0.writeAction("slorii X17 X17 12 3317")
    tran0.writeAction("slorii X17 X17 12 1493")
    tran0.writeAction("slorii X17 X17 12 846")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
