from EFA_v2 import *
def mod_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8201132248008660554, 4286427026813273517]
    tran0.writeAction("movir X16 29136")
    tran0.writeAction("slorii X16 X16 12 1125")
    tran0.writeAction("slorii X16 X16 12 1022")
    tran0.writeAction("slorii X16 X16 12 2281")
    tran0.writeAction("slorii X16 X16 12 1610")
    tran0.writeAction("movir X17 15228")
    tran0.writeAction("slorii X17 X17 12 1834")
    tran0.writeAction("slorii X17 X17 12 2976")
    tran0.writeAction("slorii X17 X17 12 3436")
    tran0.writeAction("slorii X17 X17 12 1453")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
