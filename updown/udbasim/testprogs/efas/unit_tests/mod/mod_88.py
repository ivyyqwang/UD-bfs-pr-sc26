from EFA_v2 import *
def mod_88():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4119664687593044894, 5628122090146432165]
    tran0.writeAction("movir X16 14635")
    tran0.writeAction("slorii X16 X16 12 4051")
    tran0.writeAction("slorii X16 X16 12 1241")
    tran0.writeAction("slorii X16 X16 12 2883")
    tran0.writeAction("slorii X16 X16 12 2974")
    tran0.writeAction("movir X17 19995")
    tran0.writeAction("slorii X17 X17 12 435")
    tran0.writeAction("slorii X17 X17 12 2255")
    tran0.writeAction("slorii X17 X17 12 2896")
    tran0.writeAction("slorii X17 X17 12 1189")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
