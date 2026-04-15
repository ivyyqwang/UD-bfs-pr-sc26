from EFA_v2 import *
def vdiv_32_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3774917580, 3114022134, 1017727937, 3697901716, 4180838553, 1593807928, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2969")
    tran0.writeAction("slorii X19 X19 12 3124")
    tran0.writeAction("slorii X19 X19 8 246")
    tran0.writeAction("slorii X19 X19 12 3600")
    tran0.writeAction("slorii X19 X19 12 171")
    tran0.writeAction("slorii X19 X19 8 204")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3526")
    tran0.writeAction("slorii X17 X17 12 2432")
    tran0.writeAction("slorii X17 X17 8 148")
    tran0.writeAction("slorii X17 X17 12 970")
    tran0.writeAction("slorii X17 X17 12 2379")
    tran0.writeAction("slorii X17 X17 8 193")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1519")
    tran0.writeAction("slorii X18 X18 12 3988")
    tran0.writeAction("slorii X18 X18 8 56")
    tran0.writeAction("slorii X18 X18 12 3987")
    tran0.writeAction("slorii X18 X18 12 648")
    tran0.writeAction("slorii X18 X18 8 153")
    tran0.writeAction("vdiv.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
