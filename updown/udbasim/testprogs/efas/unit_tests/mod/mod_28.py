from EFA_v2 import *
def mod_28():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5356233874300402648, -1506587459652747310]
    tran0.writeAction("movir X16 19029")
    tran0.writeAction("slorii X16 X16 12 677")
    tran0.writeAction("slorii X16 X16 12 1155")
    tran0.writeAction("slorii X16 X16 12 2415")
    tran0.writeAction("slorii X16 X16 12 3032")
    tran0.writeAction("movir X17 60183")
    tran0.writeAction("slorii X17 X17 12 2155")
    tran0.writeAction("slorii X17 X17 12 12")
    tran0.writeAction("slorii X17 X17 12 1391")
    tran0.writeAction("slorii X17 X17 12 4050")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
