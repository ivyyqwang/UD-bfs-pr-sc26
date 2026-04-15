from EFA_v2 import *
def vmadd_32_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [716241971, 1310205622, 494050910, 3380640475, 304112814, 649524821, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1249")
    tran0.writeAction("slorii X19 X19 12 2086")
    tran0.writeAction("slorii X19 X19 8 182")
    tran0.writeAction("slorii X19 X19 12 683")
    tran0.writeAction("slorii X19 X19 12 252")
    tran0.writeAction("slorii X19 X19 8 51")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3224")
    tran0.writeAction("slorii X17 X17 12 122")
    tran0.writeAction("slorii X17 X17 8 219")
    tran0.writeAction("slorii X17 X17 12 471")
    tran0.writeAction("slorii X17 X17 12 670")
    tran0.writeAction("slorii X17 X17 8 94")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 619")
    tran0.writeAction("slorii X18 X18 12 1782")
    tran0.writeAction("slorii X18 X18 8 85")
    tran0.writeAction("slorii X18 X18 12 290")
    tran0.writeAction("slorii X18 X18 12 100")
    tran0.writeAction("slorii X18 X18 8 174")
    tran0.writeAction("vmadd.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
