from EFA_v2 import *
def div_65():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5067967620751405807, -4836645725180617748]
    tran0.writeAction("movir X16 18005")
    tran0.writeAction("slorii X16 X16 12 155")
    tran0.writeAction("slorii X16 X16 12 808")
    tran0.writeAction("slorii X16 X16 12 283")
    tran0.writeAction("slorii X16 X16 12 751")
    tran0.writeAction("movir X17 48352")
    tran0.writeAction("slorii X17 X17 12 3205")
    tran0.writeAction("slorii X17 X17 12 1710")
    tran0.writeAction("slorii X17 X17 12 809")
    tran0.writeAction("slorii X17 X17 12 3052")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
