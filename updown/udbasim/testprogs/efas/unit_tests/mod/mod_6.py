from EFA_v2 import *
def mod_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3367717798412411051, -6224066846163405675]
    tran0.writeAction("movir X16 11964")
    tran0.writeAction("slorii X16 X16 12 2199")
    tran0.writeAction("slorii X16 X16 12 3750")
    tran0.writeAction("slorii X16 X16 12 542")
    tran0.writeAction("slorii X16 X16 12 171")
    tran0.writeAction("movir X17 43423")
    tran0.writeAction("slorii X17 X17 12 2754")
    tran0.writeAction("slorii X17 X17 12 3600")
    tran0.writeAction("slorii X17 X17 12 591")
    tran0.writeAction("slorii X17 X17 12 1173")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
