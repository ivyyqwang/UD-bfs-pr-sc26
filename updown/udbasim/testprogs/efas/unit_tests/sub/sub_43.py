from EFA_v2 import *
def sub_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-701222348303159431, 4745294666466427290]
    tran0.writeAction("movir X16 63044")
    tran0.writeAction("slorii X16 X16 12 3103")
    tran0.writeAction("slorii X16 X16 12 3404")
    tran0.writeAction("slorii X16 X16 12 3378")
    tran0.writeAction("slorii X16 X16 12 3961")
    tran0.writeAction("movir X17 16858")
    tran0.writeAction("slorii X17 X17 12 2757")
    tran0.writeAction("slorii X17 X17 12 2949")
    tran0.writeAction("slorii X17 X17 12 1176")
    tran0.writeAction("slorii X17 X17 12 410")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
