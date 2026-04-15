from EFA_v2 import *
def vsub_32_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3365384688, 3208255288, 3677195578, 3446501881, 1869545880, 4261052948, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3059")
    tran0.writeAction("slorii X19 X19 12 2583")
    tran0.writeAction("slorii X19 X19 8 56")
    tran0.writeAction("slorii X19 X19 12 3209")
    tran0.writeAction("slorii X19 X19 12 1969")
    tran0.writeAction("slorii X19 X19 8 240")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3286")
    tran0.writeAction("slorii X17 X17 12 3441")
    tran0.writeAction("slorii X17 X17 8 249")
    tran0.writeAction("slorii X17 X17 12 3506")
    tran0.writeAction("slorii X17 X17 12 3469")
    tran0.writeAction("slorii X17 X17 8 58")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 4063")
    tran0.writeAction("slorii X18 X18 12 2690")
    tran0.writeAction("slorii X18 X18 8 20")
    tran0.writeAction("slorii X18 X18 12 1782")
    tran0.writeAction("slorii X18 X18 12 3841")
    tran0.writeAction("slorii X18 X18 8 152")
    tran0.writeAction("vsub.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
