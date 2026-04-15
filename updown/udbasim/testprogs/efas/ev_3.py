from EFA_v2 import *
def ev_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
        "finish_events": 380546
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -16040")
    tran0.writeAction("slorii X16 X16 12 2846")
    tran0.writeAction("slorii X16 X16 12 458")
    tran0.writeAction("slorii X16 X16 12 2717")
    tran0.writeAction("slorii X16 X16 12 1400")
    tran0.writeAction("movir X17 27187")
    tran0.writeAction("slorii X17 X17 12 2265")
    tran0.writeAction("slorii X17 X17 12 2294")
    tran0.writeAction("slorii X17 X17 12 2451")
    tran0.writeAction("slorii X17 X17 12 1665")
    tran0.writeAction("movir X18 12976")
    tran0.writeAction("slorii X18 X18 12 3293")
    tran0.writeAction("slorii X18 X18 12 3731")
    tran0.writeAction("slorii X18 X18 12 2652")
    tran0.writeAction("slorii X18 X18 12 3714")
    tran0.writeAction("movir X19 -20066")
    tran0.writeAction("slorii X19 X19 12 1001")
    tran0.writeAction("slorii X19 X19 12 1868")
    tran0.writeAction("slorii X19 X19 12 3174")
    tran0.writeAction("slorii X19 X19 12 1636")
    tran0.writeAction("ev X16 X17 X18 X19 8")
    tran0.writeAction(f"print '%d,%d,%d,%d' X16 X17 X18 X19")
    tran0.writeAction("yieldt")
    tran0 = state.writeTransition("eventCarry", state, state, event_map['finish_events'])
    tran0.writeAction("yieldt")
    return efa
