from EFA_v2 import *
def vsub_i32_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1578888369, 1147200166, 647912644, -640484049, -1626383270, -1993044569, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1094")
    tran0.writeAction("slorii X19 X19 12 226")
    tran0.writeAction("slorii X19 X19 8 166")
    tran0.writeAction("slorii X19 X19 12 2590")
    tran0.writeAction("slorii X19 X19 12 1043")
    tran0.writeAction("slorii X19 X19 8 79")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3485")
    tran0.writeAction("slorii X17 X17 12 765")
    tran0.writeAction("slorii X17 X17 8 47")
    tran0.writeAction("slorii X17 X17 12 617")
    tran0.writeAction("slorii X17 X17 12 3676")
    tran0.writeAction("slorii X17 X17 8 196")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2195")
    tran0.writeAction("slorii X18 X18 12 1165")
    tran0.writeAction("slorii X18 X18 8 167")
    tran0.writeAction("slorii X18 X18 12 2544")
    tran0.writeAction("slorii X18 X18 12 3932")
    tran0.writeAction("slorii X18 X18 8 90")
    tran0.writeAction("vsub.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
