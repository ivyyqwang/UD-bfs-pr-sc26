from EFA_v2 import *
def vmul_b16_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [55075, 16537, 19045, 16741, 36991, 16220, 18115, 24583, 44951, 38216, 58754, 3102, 15]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1046")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("slorii X19 X19 12 1190")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("slorii X19 X19 12 1033")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 3442")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1536")
    tran0.writeAction("slorii X17 X17 4 7")
    tran0.writeAction("slorii X17 X17 12 1132")
    tran0.writeAction("slorii X17 X17 4 3")
    tran0.writeAction("slorii X17 X17 12 1013")
    tran0.writeAction("slorii X17 X17 4 12")
    tran0.writeAction("slorii X17 X17 12 2311")
    tran0.writeAction("slorii X17 X17 4 15")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 193")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("slorii X18 X18 12 3672")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("slorii X18 X18 12 2388")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 2809")
    tran0.writeAction("slorii X18 X18 4 7")
    tran0.writeAction("vmul.b16 X19 X17 X18 15 ")
    tran0.writeAction("yieldt")
    return efa
