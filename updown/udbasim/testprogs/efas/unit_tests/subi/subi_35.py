from EFA_v2 import *
def subi_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4770342624327366860, 12913]
    tran0.writeAction("movir X16 48588")
    tran0.writeAction("slorii X16 X16 12 1386")
    tran0.writeAction("slorii X16 X16 12 2132")
    tran0.writeAction("slorii X16 X16 12 256")
    tran0.writeAction("slorii X16 X16 12 1844")
    tran0.writeAction("subi X16 X17 12913")
    tran0.writeAction("yieldt")
    return efa
