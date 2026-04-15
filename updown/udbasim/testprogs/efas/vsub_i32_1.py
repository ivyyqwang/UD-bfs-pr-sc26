from EFA_v2 import *
def vsub_i32_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1107476011, -2008227949, 119951098, 1040439511, 932781671, 1815650024, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2180")
    tran0.writeAction("slorii X19 X19 12 3295")
    tran0.writeAction("slorii X19 X19 8 147")
    tran0.writeAction("slorii X19 X19 12 3039")
    tran0.writeAction("slorii X19 X19 12 3393")
    tran0.writeAction("slorii X19 X19 8 213")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 992")
    tran0.writeAction("slorii X17 X17 12 984")
    tran0.writeAction("slorii X17 X17 8 215")
    tran0.writeAction("slorii X17 X17 12 114")
    tran0.writeAction("slorii X17 X17 12 1614")
    tran0.writeAction("slorii X17 X17 8 250")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1731")
    tran0.writeAction("slorii X18 X18 12 2206")
    tran0.writeAction("slorii X18 X18 8 232")
    tran0.writeAction("slorii X18 X18 12 889")
    tran0.writeAction("slorii X18 X18 12 2334")
    tran0.writeAction("slorii X18 X18 8 103")
    tran0.writeAction("vsub.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
