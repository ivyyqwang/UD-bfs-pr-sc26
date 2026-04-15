from EFA_v2 import *
def mul_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7661864715374447804, -4676619809771407179]
    tran0.writeAction("movir X16 38315")
    tran0.writeAction("slorii X16 X16 12 2410")
    tran0.writeAction("slorii X16 X16 12 699")
    tran0.writeAction("slorii X16 X16 12 27")
    tran0.writeAction("slorii X16 X16 12 836")
    tran0.writeAction("movir X17 48921")
    tran0.writeAction("slorii X17 X17 12 1264")
    tran0.writeAction("slorii X17 X17 12 3985")
    tran0.writeAction("slorii X17 X17 12 83")
    tran0.writeAction("slorii X17 X17 12 2229")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
