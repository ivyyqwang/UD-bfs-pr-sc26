from EFA_v2 import *
def fmul_64_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16517011948638431341, 4224362712437751440]
    tran0.writeAction("movir X16 58680")
    tran0.writeAction("slorii X16 X16 12 877")
    tran0.writeAction("slorii X16 X16 12 2877")
    tran0.writeAction("slorii X16 X16 12 1950")
    tran0.writeAction("slorii X16 X16 12 2157")
    tran0.writeAction("movir X17 15007")
    tran0.writeAction("slorii X17 X17 12 3896")
    tran0.writeAction("slorii X17 X17 12 349")
    tran0.writeAction("slorii X17 X17 12 1055")
    tran0.writeAction("slorii X17 X17 12 3728")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
