from EFA_v2 import *
def fsub_64_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6365102425670826377, 10628875286219945066]
    tran0.writeAction("movir X16 22613")
    tran0.writeAction("slorii X16 X16 12 1582")
    tran0.writeAction("slorii X16 X16 12 3761")
    tran0.writeAction("slorii X16 X16 12 355")
    tran0.writeAction("slorii X16 X16 12 2441")
    tran0.writeAction("movir X17 37761")
    tran0.writeAction("slorii X17 X17 12 1436")
    tran0.writeAction("slorii X17 X17 12 565")
    tran0.writeAction("slorii X17 X17 12 279")
    tran0.writeAction("slorii X17 X17 12 1130")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
