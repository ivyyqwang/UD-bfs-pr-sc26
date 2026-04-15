from EFA_v2 import *
def ev_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
        "finish_events": 270718
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 12315")
    tran0.writeAction("slorii X16 X16 12 2943")
    tran0.writeAction("slorii X16 X16 12 1219")
    tran0.writeAction("slorii X16 X16 12 826")
    tran0.writeAction("slorii X16 X16 12 801")
    tran0.writeAction("movir X17 -4060")
    tran0.writeAction("slorii X17 X17 12 3087")
    tran0.writeAction("slorii X17 X17 12 1946")
    tran0.writeAction("slorii X17 X17 12 1834")
    tran0.writeAction("slorii X17 X17 12 110")
    tran0.writeAction("movir X18 -16398")
    tran0.writeAction("slorii X18 X18 12 205")
    tran0.writeAction("slorii X18 X18 12 2601")
    tran0.writeAction("slorii X18 X18 12 2370")
    tran0.writeAction("slorii X18 X18 12 382")
    tran0.writeAction("movir X19 -8248")
    tran0.writeAction("slorii X19 X19 12 277")
    tran0.writeAction("slorii X19 X19 12 1457")
    tran0.writeAction("slorii X19 X19 12 3005")
    tran0.writeAction("slorii X19 X19 12 2922")
    tran0.writeAction("ev X16 X17 X18 X19 1")
    tran0.writeAction(f"print '%d,%d,%d,%d' X16 X17 X18 X19")
    tran0.writeAction("yieldt")
    tran0 = state.writeTransition("eventCarry", state, state, event_map['finish_events'])
    tran0.writeAction("yieldt")
    return efa
