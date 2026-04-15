from EFA_v2 import *
def vsub_i32_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-251999869, 1266099915, 1918475832, 1421200006, -39935960, -234006943, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1207")
    tran0.writeAction("slorii X19 X19 12 1830")
    tran0.writeAction("slorii X19 X19 8 203")
    tran0.writeAction("slorii X19 X19 12 3855")
    tran0.writeAction("slorii X19 X19 12 2761")
    tran0.writeAction("slorii X19 X19 8 131")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1355")
    tran0.writeAction("slorii X17 X17 12 1482")
    tran0.writeAction("slorii X17 X17 8 134")
    tran0.writeAction("slorii X17 X17 12 1829")
    tran0.writeAction("slorii X17 X17 12 2462")
    tran0.writeAction("slorii X17 X17 8 56")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3872")
    tran0.writeAction("slorii X18 X18 12 3414")
    tran0.writeAction("slorii X18 X18 8 97")
    tran0.writeAction("slorii X18 X18 12 4057")
    tran0.writeAction("slorii X18 X18 12 3744")
    tran0.writeAction("slorii X18 X18 8 40")
    tran0.writeAction("vsub.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
