from EFA_v2 import *
def divi_98():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1129618281964957058, -21856]
    tran0.writeAction("movir X16 61522")
    tran0.writeAction("slorii X16 X16 12 3234")
    tran0.writeAction("slorii X16 X16 12 2131")
    tran0.writeAction("slorii X16 X16 12 2833")
    tran0.writeAction("slorii X16 X16 12 638")
    tran0.writeAction("divi X16 X17 -21856")
    tran0.writeAction("yieldt")
    return efa
