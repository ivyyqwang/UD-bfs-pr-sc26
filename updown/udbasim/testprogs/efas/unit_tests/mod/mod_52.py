from EFA_v2 import *
def mod_52():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8123138613522746194, -4865621481852183130]
    tran0.writeAction("movir X16 28859")
    tran0.writeAction("slorii X16 X16 12 760")
    tran0.writeAction("slorii X16 X16 12 2016")
    tran0.writeAction("slorii X16 X16 12 1156")
    tran0.writeAction("slorii X16 X16 12 2898")
    tran0.writeAction("movir X17 48249")
    tran0.writeAction("slorii X17 X17 12 3440")
    tran0.writeAction("slorii X17 X17 12 2714")
    tran0.writeAction("slorii X17 X17 12 2829")
    tran0.writeAction("slorii X17 X17 12 3494")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
