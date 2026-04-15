from EFA_v2 import *
def vsub_i32_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1672846298, 1646897767, 475548224, 832979269, -1873226700, -312014533, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1570")
    tran0.writeAction("slorii X19 X19 12 2474")
    tran0.writeAction("slorii X19 X19 8 103")
    tran0.writeAction("slorii X19 X19 12 1595")
    tran0.writeAction("slorii X19 X19 12 1435")
    tran0.writeAction("slorii X19 X19 8 218")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 794")
    tran0.writeAction("slorii X17 X17 12 1601")
    tran0.writeAction("slorii X17 X17 8 69")
    tran0.writeAction("slorii X17 X17 12 453")
    tran0.writeAction("slorii X17 X17 12 2122")
    tran0.writeAction("slorii X17 X17 8 64")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3798")
    tran0.writeAction("slorii X18 X18 12 1801")
    tran0.writeAction("slorii X18 X18 8 59")
    tran0.writeAction("slorii X18 X18 12 2309")
    tran0.writeAction("slorii X18 X18 12 2260")
    tran0.writeAction("slorii X18 X18 8 52")
    tran0.writeAction("vsub.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
