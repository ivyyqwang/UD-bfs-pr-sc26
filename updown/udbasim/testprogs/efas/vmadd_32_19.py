from EFA_v2 import *
def vmadd_32_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2125612049, 1112892656, 2223640362, 1514968177, 3462181302, 938223985, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1061")
    tran0.writeAction("slorii X19 X19 12 1380")
    tran0.writeAction("slorii X19 X19 8 240")
    tran0.writeAction("slorii X19 X19 12 2027")
    tran0.writeAction("slorii X19 X19 12 580")
    tran0.writeAction("slorii X19 X19 8 17")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1444")
    tran0.writeAction("slorii X17 X17 12 3220")
    tran0.writeAction("slorii X17 X17 8 113")
    tran0.writeAction("slorii X17 X17 12 2120")
    tran0.writeAction("slorii X17 X17 12 2575")
    tran0.writeAction("slorii X17 X17 8 42")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 894")
    tran0.writeAction("slorii X18 X18 12 3113")
    tran0.writeAction("slorii X18 X18 8 113")
    tran0.writeAction("slorii X18 X18 12 3301")
    tran0.writeAction("slorii X18 X18 12 3249")
    tran0.writeAction("slorii X18 X18 8 182")
    tran0.writeAction("vmadd.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
