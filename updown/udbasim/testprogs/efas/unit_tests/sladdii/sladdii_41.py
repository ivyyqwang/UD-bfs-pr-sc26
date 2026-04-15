from EFA_v2 import *
def sladdii_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5273830997426938665, 10, 831]
    tran0.writeAction("movir X16 46799")
    tran0.writeAction("slorii X16 X16 12 2410")
    tran0.writeAction("slorii X16 X16 12 1624")
    tran0.writeAction("slorii X16 X16 12 3781")
    tran0.writeAction("slorii X16 X16 12 3287")
    tran0.writeAction("sladdii X16 X17 10 831")
    tran0.writeAction("yieldt")
    return efa
