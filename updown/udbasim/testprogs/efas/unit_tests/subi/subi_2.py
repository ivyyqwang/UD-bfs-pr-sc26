from EFA_v2 import *
def subi_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8034429595973270274, -23174]
    tran0.writeAction("movir X16 28544")
    tran0.writeAction("slorii X16 X16 12 114")
    tran0.writeAction("slorii X16 X16 12 1592")
    tran0.writeAction("slorii X16 X16 12 3571")
    tran0.writeAction("slorii X16 X16 12 2818")
    tran0.writeAction("subi X16 X17 -23174")
    tran0.writeAction("yieldt")
    return efa
