from EFA_v2 import *
def vgt_32_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3673294581, 87831198, 4065936328, 3048157655, 3013459850, 48606563, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 83")
    tran0.writeAction("slorii X19 X19 12 3122")
    tran0.writeAction("slorii X19 X19 8 158")
    tran0.writeAction("slorii X19 X19 12 3503")
    tran0.writeAction("slorii X19 X19 12 518")
    tran0.writeAction("slorii X19 X19 8 245")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2906")
    tran0.writeAction("slorii X17 X17 12 3889")
    tran0.writeAction("slorii X17 X17 8 215")
    tran0.writeAction("slorii X17 X17 12 3877")
    tran0.writeAction("slorii X17 X17 12 2371")
    tran0.writeAction("slorii X17 X17 8 200")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 46")
    tran0.writeAction("slorii X18 X18 12 1453")
    tran0.writeAction("slorii X18 X18 8 99")
    tran0.writeAction("slorii X18 X18 12 2873")
    tran0.writeAction("slorii X18 X18 12 3519")
    tran0.writeAction("slorii X18 X18 8 138")
    tran0.writeAction("vgt.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
