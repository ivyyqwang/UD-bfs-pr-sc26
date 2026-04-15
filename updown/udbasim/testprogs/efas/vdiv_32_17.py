from EFA_v2 import *
def vdiv_32_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3731968709, 2417462622, 1994394776, 3813847931, 3143264956, 902624577, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2305")
    tran0.writeAction("slorii X19 X19 12 1933")
    tran0.writeAction("slorii X19 X19 8 94")
    tran0.writeAction("slorii X19 X19 12 3559")
    tran0.writeAction("slorii X19 X19 12 338")
    tran0.writeAction("slorii X19 X19 8 197")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3637")
    tran0.writeAction("slorii X17 X17 12 691")
    tran0.writeAction("slorii X17 X17 8 123")
    tran0.writeAction("slorii X17 X17 12 1902")
    tran0.writeAction("slorii X17 X17 12 12")
    tran0.writeAction("slorii X17 X17 8 152")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 860")
    tran0.writeAction("slorii X18 X18 12 3317")
    tran0.writeAction("slorii X18 X18 8 65")
    tran0.writeAction("slorii X18 X18 12 2997")
    tran0.writeAction("slorii X18 X18 12 2666")
    tran0.writeAction("slorii X18 X18 8 188")
    tran0.writeAction("vdiv.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
