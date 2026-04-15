from EFA_v2 import *
def vsub_32_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1346650212, 629915158, 1498234056, 1548044606, 1581378851, 540348968, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 600")
    tran0.writeAction("slorii X19 X19 12 3006")
    tran0.writeAction("slorii X19 X19 8 22")
    tran0.writeAction("slorii X19 X19 12 1284")
    tran0.writeAction("slorii X19 X19 12 1088")
    tran0.writeAction("slorii X19 X19 8 100")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1476")
    tran0.writeAction("slorii X17 X17 12 1353")
    tran0.writeAction("slorii X17 X17 8 62")
    tran0.writeAction("slorii X17 X17 12 1428")
    tran0.writeAction("slorii X17 X17 12 3388")
    tran0.writeAction("slorii X17 X17 8 200")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 515")
    tran0.writeAction("slorii X18 X18 12 1298")
    tran0.writeAction("slorii X18 X18 8 40")
    tran0.writeAction("slorii X18 X18 12 1508")
    tran0.writeAction("slorii X18 X18 12 493")
    tran0.writeAction("slorii X18 X18 8 35")
    tran0.writeAction("vsub.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
