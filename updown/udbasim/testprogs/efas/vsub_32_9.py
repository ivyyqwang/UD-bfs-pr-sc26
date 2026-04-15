from EFA_v2 import *
def vsub_32_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3335943138, 837786813, 2716219426, 52130958, 323792734, 817529518, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 798")
    tran0.writeAction("slorii X19 X19 12 3996")
    tran0.writeAction("slorii X19 X19 8 189")
    tran0.writeAction("slorii X19 X19 12 3181")
    tran0.writeAction("slorii X19 X19 12 1651")
    tran0.writeAction("slorii X19 X19 8 226")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 49")
    tran0.writeAction("slorii X17 X17 12 2932")
    tran0.writeAction("slorii X17 X17 8 142")
    tran0.writeAction("slorii X17 X17 12 2590")
    tran0.writeAction("slorii X17 X17 12 1592")
    tran0.writeAction("slorii X17 X17 8 34")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 779")
    tran0.writeAction("slorii X18 X18 12 2690")
    tran0.writeAction("slorii X18 X18 8 174")
    tran0.writeAction("slorii X18 X18 12 308")
    tran0.writeAction("slorii X18 X18 12 3247")
    tran0.writeAction("slorii X18 X18 8 94")
    tran0.writeAction("vsub.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
