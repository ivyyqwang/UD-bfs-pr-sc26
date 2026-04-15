from EFA_v2 import *
def vsub_32_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [552807571, 952384249, 1058481428, 2289899481, 2321016263, 1075815016, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 908")
    tran0.writeAction("slorii X19 X19 12 1082")
    tran0.writeAction("slorii X19 X19 8 249")
    tran0.writeAction("slorii X19 X19 12 527")
    tran0.writeAction("slorii X19 X19 12 812")
    tran0.writeAction("slorii X19 X19 8 147")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2183")
    tran0.writeAction("slorii X17 X17 12 3351")
    tran0.writeAction("slorii X17 X17 8 217")
    tran0.writeAction("slorii X17 X17 12 1009")
    tran0.writeAction("slorii X17 X17 12 1829")
    tran0.writeAction("slorii X17 X17 8 20")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1025")
    tran0.writeAction("slorii X18 X18 12 4002")
    tran0.writeAction("slorii X18 X18 8 104")
    tran0.writeAction("slorii X18 X18 12 2213")
    tran0.writeAction("slorii X18 X18 12 2021")
    tran0.writeAction("slorii X18 X18 8 199")
    tran0.writeAction("vsub.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
