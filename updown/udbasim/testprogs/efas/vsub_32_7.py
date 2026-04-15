from EFA_v2 import *
def vsub_32_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3160889521, 957491938, 3683031233, 3744645911, 1028578294, 1500304789, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 913")
    tran0.writeAction("slorii X19 X19 12 554")
    tran0.writeAction("slorii X19 X19 8 226")
    tran0.writeAction("slorii X19 X19 12 3014")
    tran0.writeAction("slorii X19 X19 12 1880")
    tran0.writeAction("slorii X19 X19 8 177")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3571")
    tran0.writeAction("slorii X17 X17 12 707")
    tran0.writeAction("slorii X17 X17 8 23")
    tran0.writeAction("slorii X17 X17 12 3512")
    tran0.writeAction("slorii X17 X17 12 1688")
    tran0.writeAction("slorii X17 X17 8 193")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1430")
    tran0.writeAction("slorii X18 X18 12 3285")
    tran0.writeAction("slorii X18 X18 8 149")
    tran0.writeAction("slorii X18 X18 12 980")
    tran0.writeAction("slorii X18 X18 12 3803")
    tran0.writeAction("slorii X18 X18 8 246")
    tran0.writeAction("vsub.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
