from EFA_v2 import *
def fsub_64_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2111882657748789817, 8395869500247104565]
    tran0.writeAction("movir X16 7502")
    tran0.writeAction("slorii X16 X16 12 3745")
    tran0.writeAction("slorii X16 X16 12 1670")
    tran0.writeAction("slorii X16 X16 12 1738")
    tran0.writeAction("slorii X16 X16 12 2617")
    tran0.writeAction("movir X17 29828")
    tran0.writeAction("slorii X17 X17 12 493")
    tran0.writeAction("slorii X17 X17 12 966")
    tran0.writeAction("slorii X17 X17 12 3133")
    tran0.writeAction("slorii X17 X17 12 3125")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
