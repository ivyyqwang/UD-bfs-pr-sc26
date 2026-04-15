from EFA_v2 import *
def vdiv_32_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3892300902, 1440076385, 2997505248, 3016919149, 1314576026, 106909165, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1373")
    tran0.writeAction("slorii X19 X19 12 1490")
    tran0.writeAction("slorii X19 X19 8 97")
    tran0.writeAction("slorii X19 X19 12 3711")
    tran0.writeAction("slorii X19 X19 12 4044")
    tran0.writeAction("slorii X19 X19 8 102")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2877")
    tran0.writeAction("slorii X17 X17 12 648")
    tran0.writeAction("slorii X17 X17 8 109")
    tran0.writeAction("slorii X17 X17 12 2858")
    tran0.writeAction("slorii X17 X17 12 2636")
    tran0.writeAction("slorii X17 X17 8 224")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 101")
    tran0.writeAction("slorii X18 X18 12 3917")
    tran0.writeAction("slorii X18 X18 8 237")
    tran0.writeAction("slorii X18 X18 12 1253")
    tran0.writeAction("slorii X18 X18 12 2774")
    tran0.writeAction("slorii X18 X18 8 154")
    tran0.writeAction("vdiv.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
