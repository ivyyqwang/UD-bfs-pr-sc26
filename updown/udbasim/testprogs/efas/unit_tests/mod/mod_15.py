from EFA_v2 import *
def mod_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6754061986997777351, 8590292716632496037]
    tran0.writeAction("movir X16 23995")
    tran0.writeAction("slorii X16 X16 12 1017")
    tran0.writeAction("slorii X16 X16 12 1973")
    tran0.writeAction("slorii X16 X16 12 3979")
    tran0.writeAction("slorii X16 X16 12 967")
    tran0.writeAction("movir X17 30518")
    tran0.writeAction("slorii X17 X17 12 3483")
    tran0.writeAction("slorii X17 X17 12 1635")
    tran0.writeAction("slorii X17 X17 12 2069")
    tran0.writeAction("slorii X17 X17 12 1957")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
