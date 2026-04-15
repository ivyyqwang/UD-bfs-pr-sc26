from EFA_v2 import *
def vdiv_i32_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-691747634, -692739986, 2144322416, -79448895, -1047605046, 1494069448, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3435")
    tran0.writeAction("slorii X19 X19 12 1440")
    tran0.writeAction("slorii X19 X19 8 110")
    tran0.writeAction("slorii X19 X19 12 3436")
    tran0.writeAction("slorii X19 X19 12 1220")
    tran0.writeAction("slorii X19 X19 8 206")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 4020")
    tran0.writeAction("slorii X17 X17 12 948")
    tran0.writeAction("slorii X17 X17 8 193")
    tran0.writeAction("slorii X17 X17 12 2044")
    tran0.writeAction("slorii X17 X17 12 4035")
    tran0.writeAction("slorii X17 X17 8 112")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1424")
    tran0.writeAction("slorii X18 X18 12 3504")
    tran0.writeAction("slorii X18 X18 8 200")
    tran0.writeAction("slorii X18 X18 12 3096")
    tran0.writeAction("slorii X18 X18 12 3792")
    tran0.writeAction("slorii X18 X18 8 202")
    tran0.writeAction("vdiv.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
