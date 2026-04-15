from EFA_v2 import *
def vsub_i32_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [409298367, -279256003, 655449188, 1878977416, -50414131, -182545464, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3829")
    tran0.writeAction("slorii X19 X19 12 2788")
    tran0.writeAction("slorii X19 X19 8 61")
    tran0.writeAction("slorii X19 X19 12 390")
    tran0.writeAction("slorii X19 X19 12 1381")
    tran0.writeAction("slorii X19 X19 8 191")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1791")
    tran0.writeAction("slorii X17 X17 12 3819")
    tran0.writeAction("slorii X17 X17 8 136")
    tran0.writeAction("slorii X17 X17 12 625")
    tran0.writeAction("slorii X17 X17 12 348")
    tran0.writeAction("slorii X17 X17 8 100")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3921")
    tran0.writeAction("slorii X18 X18 12 3731")
    tran0.writeAction("slorii X18 X18 8 200")
    tran0.writeAction("slorii X18 X18 12 4047")
    tran0.writeAction("slorii X18 X18 12 3773")
    tran0.writeAction("slorii X18 X18 8 205")
    tran0.writeAction("vsub.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
