from EFA_v2 import *
def sub_69():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7440874557037035758, 2094459381861577805]
    tran0.writeAction("movir X16 39100")
    tran0.writeAction("slorii X16 X16 12 2880")
    tran0.writeAction("slorii X16 X16 12 905")
    tran0.writeAction("slorii X16 X16 12 2315")
    tran0.writeAction("slorii X16 X16 12 3858")
    tran0.writeAction("movir X17 7441")
    tran0.writeAction("slorii X17 X17 12 59")
    tran0.writeAction("slorii X17 X17 12 1532")
    tran0.writeAction("slorii X17 X17 12 1407")
    tran0.writeAction("slorii X17 X17 12 1101")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
