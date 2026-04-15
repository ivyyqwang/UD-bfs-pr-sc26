from EFA_v2 import *
def vmadd_32_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2585284774, 778603600, 3599183112, 2930760144, 384541185, 1271584260, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 742")
    tran0.writeAction("slorii X19 X19 12 2188")
    tran0.writeAction("slorii X19 X19 8 80")
    tran0.writeAction("slorii X19 X19 12 2465")
    tran0.writeAction("slorii X19 X19 12 2128")
    tran0.writeAction("slorii X19 X19 8 166")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2794")
    tran0.writeAction("slorii X17 X17 12 4057")
    tran0.writeAction("slorii X17 X17 8 208")
    tran0.writeAction("slorii X17 X17 12 3432")
    tran0.writeAction("slorii X17 X17 12 1837")
    tran0.writeAction("slorii X17 X17 8 8")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1212")
    tran0.writeAction("slorii X18 X18 12 2774")
    tran0.writeAction("slorii X18 X18 8 4")
    tran0.writeAction("slorii X18 X18 12 366")
    tran0.writeAction("slorii X18 X18 12 2978")
    tran0.writeAction("slorii X18 X18 8 1")
    tran0.writeAction("vmadd.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
