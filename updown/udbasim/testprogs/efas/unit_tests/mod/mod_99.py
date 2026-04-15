from EFA_v2 import *
def mod_99():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1048472926068529871, -1693386830973785966]
    tran0.writeAction("movir X16 61811")
    tran0.writeAction("slorii X16 X16 12 310")
    tran0.writeAction("slorii X16 X16 12 3525")
    tran0.writeAction("slorii X16 X16 12 290")
    tran0.writeAction("slorii X16 X16 12 1329")
    tran0.writeAction("movir X17 59519")
    tran0.writeAction("slorii X17 X17 12 3610")
    tran0.writeAction("slorii X17 X17 12 1584")
    tran0.writeAction("slorii X17 X17 12 1978")
    tran0.writeAction("slorii X17 X17 12 2194")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
