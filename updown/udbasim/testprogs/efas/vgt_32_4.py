from EFA_v2 import *
def vgt_32_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [742478846, 1893692745, 3857750955, 2354685791, 2011018713, 2879486521, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1805")
    tran0.writeAction("slorii X19 X19 12 3957")
    tran0.writeAction("slorii X19 X19 8 73")
    tran0.writeAction("slorii X19 X19 12 708")
    tran0.writeAction("slorii X19 X19 12 339")
    tran0.writeAction("slorii X19 X19 8 254")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2245")
    tran0.writeAction("slorii X17 X17 12 2471")
    tran0.writeAction("slorii X17 X17 8 95")
    tran0.writeAction("slorii X17 X17 12 3679")
    tran0.writeAction("slorii X17 X17 12 155")
    tran0.writeAction("slorii X17 X17 8 171")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2746")
    tran0.writeAction("slorii X18 X18 12 378")
    tran0.writeAction("slorii X18 X18 8 57")
    tran0.writeAction("slorii X18 X18 12 1917")
    tran0.writeAction("slorii X18 X18 12 3509")
    tran0.writeAction("slorii X18 X18 8 217")
    tran0.writeAction("vgt.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
