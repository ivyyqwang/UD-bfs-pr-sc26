from EFA_v2 import *
def vmadd_i32_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1845671312, -1304434475, -985123706, -2119303286, 1207571645, 1425834265, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2851")
    tran0.writeAction("slorii X19 X19 12 4072")
    tran0.writeAction("slorii X19 X19 8 213")
    tran0.writeAction("slorii X19 X19 12 2335")
    tran0.writeAction("slorii X19 X19 12 3402")
    tran0.writeAction("slorii X19 X19 8 112")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2074")
    tran0.writeAction("slorii X17 X17 12 3583")
    tran0.writeAction("slorii X17 X17 8 138")
    tran0.writeAction("slorii X17 X17 12 3156")
    tran0.writeAction("slorii X17 X17 12 2100")
    tran0.writeAction("slorii X17 X17 8 134")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1359")
    tran0.writeAction("slorii X18 X18 12 3201")
    tran0.writeAction("slorii X18 X18 8 25")
    tran0.writeAction("slorii X18 X18 12 1151")
    tran0.writeAction("slorii X18 X18 12 2580")
    tran0.writeAction("slorii X18 X18 8 189")
    tran0.writeAction("vmadd.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
