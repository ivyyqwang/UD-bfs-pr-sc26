from EFA_v2 import *
def mod_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5116398834146543742, -7084047435250958003]
    tran0.writeAction("movir X16 47358")
    tran0.writeAction("slorii X16 X16 12 3685")
    tran0.writeAction("slorii X16 X16 12 3649")
    tran0.writeAction("slorii X16 X16 12 1935")
    tran0.writeAction("slorii X16 X16 12 1922")
    tran0.writeAction("movir X17 40368")
    tran0.writeAction("slorii X17 X17 12 1670")
    tran0.writeAction("slorii X17 X17 12 1017")
    tran0.writeAction("slorii X17 X17 12 3480")
    tran0.writeAction("slorii X17 X17 12 333")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
