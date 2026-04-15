from EFA_v2 import *
def vsub_i32_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [773516147, 578805909, 1982046137, -186957658, -1632219566, 1275558262, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 551")
    tran0.writeAction("slorii X19 X19 12 4064")
    tran0.writeAction("slorii X19 X19 8 149")
    tran0.writeAction("slorii X19 X19 12 737")
    tran0.writeAction("slorii X19 X19 12 2795")
    tran0.writeAction("slorii X19 X19 8 115")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3917")
    tran0.writeAction("slorii X17 X17 12 2880")
    tran0.writeAction("slorii X17 X17 8 166")
    tran0.writeAction("slorii X17 X17 12 1890")
    tran0.writeAction("slorii X17 X17 12 927")
    tran0.writeAction("slorii X17 X17 8 185")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1216")
    tran0.writeAction("slorii X18 X18 12 1913")
    tran0.writeAction("slorii X18 X18 8 118")
    tran0.writeAction("slorii X18 X18 12 2539")
    tran0.writeAction("slorii X18 X18 12 1614")
    tran0.writeAction("slorii X18 X18 8 82")
    tran0.writeAction("vsub.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
