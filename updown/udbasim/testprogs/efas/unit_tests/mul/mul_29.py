from EFA_v2 import *
def mul_29():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3976331923974008100, -5075537258548736609]
    tran0.writeAction("movir X16 14126")
    tran0.writeAction("slorii X16 X16 12 3149")
    tran0.writeAction("slorii X16 X16 12 317")
    tran0.writeAction("slorii X16 X16 12 2114")
    tran0.writeAction("slorii X16 X16 12 3364")
    tran0.writeAction("movir X17 47504")
    tran0.writeAction("slorii X17 X17 12 284")
    tran0.writeAction("slorii X17 X17 12 307")
    tran0.writeAction("slorii X17 X17 12 3860")
    tran0.writeAction("slorii X17 X17 12 3487")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
