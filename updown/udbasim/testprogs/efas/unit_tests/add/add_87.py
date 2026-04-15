from EFA_v2 import *
def add_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5990049872135298707, -2032178885148074035]
    tran0.writeAction("movir X16 21280")
    tran0.writeAction("slorii X16 X16 12 3817")
    tran0.writeAction("slorii X16 X16 12 3903")
    tran0.writeAction("slorii X16 X16 12 2041")
    tran0.writeAction("slorii X16 X16 12 3731")
    tran0.writeAction("movir X17 58316")
    tran0.writeAction("slorii X17 X17 12 1025")
    tran0.writeAction("slorii X17 X17 12 550")
    tran0.writeAction("slorii X17 X17 12 2865")
    tran0.writeAction("slorii X17 X17 12 4045")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
