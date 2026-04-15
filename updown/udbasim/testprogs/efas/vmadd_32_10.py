from EFA_v2 import *
def vmadd_32_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4112744023, 1871277230, 2936564409, 2162343786, 1811224181, 1952677303, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1784")
    tran0.writeAction("slorii X19 X19 12 2412")
    tran0.writeAction("slorii X19 X19 8 174")
    tran0.writeAction("slorii X19 X19 12 3922")
    tran0.writeAction("slorii X19 X19 12 894")
    tran0.writeAction("slorii X19 X19 8 87")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2062")
    tran0.writeAction("slorii X17 X17 12 703")
    tran0.writeAction("slorii X17 X17 8 106")
    tran0.writeAction("slorii X17 X17 12 2800")
    tran0.writeAction("slorii X17 X17 12 2154")
    tran0.writeAction("slorii X17 X17 8 185")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1862")
    tran0.writeAction("slorii X18 X18 12 893")
    tran0.writeAction("slorii X18 X18 8 183")
    tran0.writeAction("slorii X18 X18 12 1727")
    tran0.writeAction("slorii X18 X18 12 1302")
    tran0.writeAction("slorii X18 X18 8 117")
    tran0.writeAction("vmadd.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
