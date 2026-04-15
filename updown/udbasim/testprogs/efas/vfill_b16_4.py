from EFA_v2 import *
def vfill_b16_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [40712, 59733, 6151, 44051, '19.25']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2753")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 384")
    tran0.writeAction("slorii X18 X18 4 7")
    tran0.writeAction("slorii X18 X18 12 3733")
    tran0.writeAction("slorii X18 X18 4 5")
    tran0.writeAction("slorii X18 X18 12 2544")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("vfill.b16 X18 19.25 ")
    tran0.writeAction("yieldt")
    return efa
