from EFA_v2 import *
def subi_98():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5391513273982681884, -21396]
    tran0.writeAction("movir X16 46381")
    tran0.writeAction("slorii X16 X16 12 2035")
    tran0.writeAction("slorii X16 X16 12 3622")
    tran0.writeAction("slorii X16 X16 12 1879")
    tran0.writeAction("slorii X16 X16 12 3300")
    tran0.writeAction("subi X16 X17 -21396")
    tran0.writeAction("yieldt")
    return efa
