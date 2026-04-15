from EFA_v2 import *
def mod_38():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6820551145940061532, 1169348741679087575]
    tran0.writeAction("movir X16 41304")
    tran0.writeAction("slorii X16 X16 12 2189")
    tran0.writeAction("slorii X16 X16 12 3741")
    tran0.writeAction("slorii X16 X16 12 3519")
    tran0.writeAction("slorii X16 X16 12 676")
    tran0.writeAction("movir X17 4154")
    tran0.writeAction("slorii X17 X17 12 1479")
    tran0.writeAction("slorii X17 X17 12 3118")
    tran0.writeAction("slorii X17 X17 12 1359")
    tran0.writeAction("slorii X17 X17 12 4055")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
