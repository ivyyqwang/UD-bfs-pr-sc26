from EFA_v2 import *
def sladdii_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8916952316145829563, 6, 1978]
    tran0.writeAction("movir X16 33856")
    tran0.writeAction("slorii X16 X16 12 2545")
    tran0.writeAction("slorii X16 X16 12 3277")
    tran0.writeAction("slorii X16 X16 12 127")
    tran0.writeAction("slorii X16 X16 12 2373")
    tran0.writeAction("sladdii X16 X17 6 1978")
    tran0.writeAction("yieldt")
    return efa
