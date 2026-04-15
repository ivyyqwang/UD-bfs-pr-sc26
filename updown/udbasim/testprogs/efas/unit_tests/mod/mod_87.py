from EFA_v2 import *
def mod_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3594615373128584652, 6751970405572376416]
    tran0.writeAction("movir X16 52765")
    tran0.writeAction("slorii X16 X16 12 1477")
    tran0.writeAction("slorii X16 X16 12 3324")
    tran0.writeAction("slorii X16 X16 12 2099")
    tran0.writeAction("slorii X16 X16 12 564")
    tran0.writeAction("movir X17 23987")
    tran0.writeAction("slorii X17 X17 12 3348")
    tran0.writeAction("slorii X17 X17 12 3958")
    tran0.writeAction("slorii X17 X17 12 375")
    tran0.writeAction("slorii X17 X17 12 1888")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
