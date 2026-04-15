from EFA_v2 import *
def vdiv_i32_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-977752583, -308583982, 1285075234, 1291935551, 2065722401, 1597985922, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3801")
    tran0.writeAction("slorii X19 X19 12 2913")
    tran0.writeAction("slorii X19 X19 8 210")
    tran0.writeAction("slorii X19 X19 12 3163")
    tran0.writeAction("slorii X19 X19 12 2221")
    tran0.writeAction("slorii X19 X19 8 249")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1232")
    tran0.writeAction("slorii X17 X17 12 351")
    tran0.writeAction("slorii X17 X17 8 63")
    tran0.writeAction("slorii X17 X17 12 1225")
    tran0.writeAction("slorii X17 X17 12 2225")
    tran0.writeAction("slorii X17 X17 8 34")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1523")
    tran0.writeAction("slorii X18 X18 12 3924")
    tran0.writeAction("slorii X18 X18 8 130")
    tran0.writeAction("slorii X18 X18 12 1970")
    tran0.writeAction("slorii X18 X18 12 108")
    tran0.writeAction("slorii X18 X18 8 33")
    tran0.writeAction("vdiv.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
