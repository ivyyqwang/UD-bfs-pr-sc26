from EFA_v2 import *
def vsub_b16_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [31353, 62238, 55096, 38686, 48524, 16648, 26165, 33041, 42096, 17706, 61041, 24657, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2417")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 3443")
    tran0.writeAction("slorii X19 X19 4 8")
    tran0.writeAction("slorii X19 X19 12 3889")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 1959")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2065")
    tran0.writeAction("slorii X17 X17 4 1")
    tran0.writeAction("slorii X17 X17 12 1635")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("slorii X17 X17 12 1040")
    tran0.writeAction("slorii X17 X17 4 8")
    tran0.writeAction("slorii X17 X17 12 3032")
    tran0.writeAction("slorii X17 X17 4 12")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1541")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("slorii X18 X18 12 3815")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("slorii X18 X18 12 1106")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 2631")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("vsub.b16 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
