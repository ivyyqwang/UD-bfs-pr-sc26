from EFA_v2 import *
def divi_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [841694834427949768, -5092]
    tran0.writeAction("movir X16 2990")
    tran0.writeAction("slorii X16 X16 12 1231")
    tran0.writeAction("slorii X16 X16 12 3599")
    tran0.writeAction("slorii X16 X16 12 1471")
    tran0.writeAction("slorii X16 X16 12 712")
    tran0.writeAction("divi X16 X17 -5092")
    tran0.writeAction("yieldt")
    return efa
