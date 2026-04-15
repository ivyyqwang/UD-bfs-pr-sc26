from EFA_v2 import *
def fdiv_64_65():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14722630823961456031, 2071547942826134236]
    tran0.writeAction("movir X16 52305")
    tran0.writeAction("slorii X16 X16 12 1195")
    tran0.writeAction("slorii X16 X16 12 2821")
    tran0.writeAction("slorii X16 X16 12 1798")
    tran0.writeAction("slorii X16 X16 12 3487")
    tran0.writeAction("movir X17 7359")
    tran0.writeAction("slorii X17 X17 12 2526")
    tran0.writeAction("slorii X17 X17 12 227")
    tran0.writeAction("slorii X17 X17 12 1404")
    tran0.writeAction("slorii X17 X17 12 2780")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
