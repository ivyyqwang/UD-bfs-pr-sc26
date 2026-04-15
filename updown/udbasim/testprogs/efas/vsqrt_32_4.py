from EFA_v2 import *
def vsqrt_32_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1672934352, 1344916005, 917410127, 4248789812, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1282")
    tran0.writeAction("slorii X19 X19 12 2506")
    tran0.writeAction("slorii X19 X19 8 37")
    tran0.writeAction("slorii X19 X19 12 1595")
    tran0.writeAction("slorii X19 X19 12 1779")
    tran0.writeAction("slorii X19 X19 8 208")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 4051")
    tran0.writeAction("slorii X18 X18 12 3939")
    tran0.writeAction("slorii X18 X18 8 52")
    tran0.writeAction("slorii X18 X18 12 874")
    tran0.writeAction("slorii X18 X18 12 3729")
    tran0.writeAction("slorii X18 X18 8 79")
    tran0.writeAction("vsqrt.32 X19 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
