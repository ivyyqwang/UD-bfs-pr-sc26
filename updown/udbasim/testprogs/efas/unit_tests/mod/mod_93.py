from EFA_v2 import *
def mod_93():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5735309605143972901, 4318473910044133264]
    tran0.writeAction("movir X16 20375")
    tran0.writeAction("slorii X16 X16 12 3739")
    tran0.writeAction("slorii X16 X16 12 747")
    tran0.writeAction("slorii X16 X16 12 2016")
    tran0.writeAction("slorii X16 X16 12 3109")
    tran0.writeAction("movir X17 15342")
    tran0.writeAction("slorii X17 X17 12 1234")
    tran0.writeAction("slorii X17 X17 12 1043")
    tran0.writeAction("slorii X17 X17 12 3984")
    tran0.writeAction("slorii X17 X17 12 1936")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
