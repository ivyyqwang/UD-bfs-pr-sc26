from EFA_v2 import *
def vmul_b16_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [58425, 34932, 40867, 40609, 25329, 14844, 29125, 51542, 7717, 39770, 44581, 59297, 15]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2538")
    tran0.writeAction("slorii X19 X19 4 1")
    tran0.writeAction("slorii X19 X19 12 2554")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 2183")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("slorii X19 X19 12 3651")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3221")
    tran0.writeAction("slorii X17 X17 4 6")
    tran0.writeAction("slorii X17 X17 12 1820")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("slorii X17 X17 12 927")
    tran0.writeAction("slorii X17 X17 4 12")
    tran0.writeAction("slorii X17 X17 12 1583")
    tran0.writeAction("slorii X17 X17 4 1")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3706")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("slorii X18 X18 12 2786")
    tran0.writeAction("slorii X18 X18 4 5")
    tran0.writeAction("slorii X18 X18 12 2485")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 482")
    tran0.writeAction("slorii X18 X18 4 5")
    tran0.writeAction("vmul.b16 X19 X17 X18 15 ")
    tran0.writeAction("yieldt")
    return efa
