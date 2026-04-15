from EFA_v2 import *
def mod_26():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8414848097938803703, -6647496373205032394]
    tran0.writeAction("movir X16 29895")
    tran0.writeAction("slorii X16 X16 12 2236")
    tran0.writeAction("slorii X16 X16 12 740")
    tran0.writeAction("slorii X16 X16 12 2104")
    tran0.writeAction("slorii X16 X16 12 3063")
    tran0.writeAction("movir X17 41919")
    tran0.writeAction("slorii X17 X17 12 1428")
    tran0.writeAction("slorii X17 X17 12 1213")
    tran0.writeAction("slorii X17 X17 12 1706")
    tran0.writeAction("slorii X17 X17 12 566")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
