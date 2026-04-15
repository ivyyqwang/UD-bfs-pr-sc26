from EFA_v2 import *
def subi_48():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6603788392289942022, -11191]
    tran0.writeAction("movir X16 42074")
    tran0.writeAction("slorii X16 X16 12 2583")
    tran0.writeAction("slorii X16 X16 12 529")
    tran0.writeAction("slorii X16 X16 12 2908")
    tran0.writeAction("slorii X16 X16 12 1530")
    tran0.writeAction("subi X16 X17 -11191")
    tran0.writeAction("yieldt")
    return efa
