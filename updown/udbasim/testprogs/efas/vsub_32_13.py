from EFA_v2 import *
def vsub_32_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3487897530, 1287525374, 145806934, 1321972632, 24410815, 2219991727, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1227")
    tran0.writeAction("slorii X19 X19 12 3603")
    tran0.writeAction("slorii X19 X19 8 254")
    tran0.writeAction("slorii X19 X19 12 3326")
    tran0.writeAction("slorii X19 X19 12 1303")
    tran0.writeAction("slorii X19 X19 8 186")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1260")
    tran0.writeAction("slorii X17 X17 12 2995")
    tran0.writeAction("slorii X17 X17 8 152")
    tran0.writeAction("slorii X17 X17 12 139")
    tran0.writeAction("slorii X17 X17 12 214")
    tran0.writeAction("slorii X17 X17 8 86")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2117")
    tran0.writeAction("slorii X18 X18 12 610")
    tran0.writeAction("slorii X18 X18 8 175")
    tran0.writeAction("slorii X18 X18 12 23")
    tran0.writeAction("slorii X18 X18 12 1146")
    tran0.writeAction("slorii X18 X18 8 191")
    tran0.writeAction("vsub.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
