from EFA_v2 import *
def mul_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7102394363253827729, 5242595293720663458]
    tran0.writeAction("movir X16 40303")
    tran0.writeAction("slorii X16 X16 12 927")
    tran0.writeAction("slorii X16 X16 12 1259")
    tran0.writeAction("slorii X16 X16 12 2125")
    tran0.writeAction("slorii X16 X16 12 1903")
    tran0.writeAction("movir X17 18625")
    tran0.writeAction("slorii X17 X17 12 1802")
    tran0.writeAction("slorii X17 X17 12 1191")
    tran0.writeAction("slorii X17 X17 12 1453")
    tran0.writeAction("slorii X17 X17 12 1442")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
