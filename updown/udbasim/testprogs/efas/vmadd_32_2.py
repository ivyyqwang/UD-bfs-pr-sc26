from EFA_v2 import *
def vmadd_32_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2597764629, 263953060, 1215943703, 1304050209, 2488481266, 2846990938, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 251")
    tran0.writeAction("slorii X19 X19 12 2970")
    tran0.writeAction("slorii X19 X19 8 164")
    tran0.writeAction("slorii X19 X19 12 2477")
    tran0.writeAction("slorii X19 X19 12 1726")
    tran0.writeAction("slorii X19 X19 8 21")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1243")
    tran0.writeAction("slorii X17 X17 12 2618")
    tran0.writeAction("slorii X17 X17 8 33")
    tran0.writeAction("slorii X17 X17 12 1159")
    tran0.writeAction("slorii X17 X17 12 2516")
    tran0.writeAction("slorii X17 X17 8 23")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2715")
    tran0.writeAction("slorii X18 X18 12 418")
    tran0.writeAction("slorii X18 X18 8 90")
    tran0.writeAction("slorii X18 X18 12 2373")
    tran0.writeAction("slorii X18 X18 12 821")
    tran0.writeAction("slorii X18 X18 8 242")
    tran0.writeAction("vmadd.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
