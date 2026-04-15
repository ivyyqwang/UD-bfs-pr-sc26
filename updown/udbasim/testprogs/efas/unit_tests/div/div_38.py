from EFA_v2 import *
def div_38():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1270672288916531539, -7447241413047363414]
    tran0.writeAction("movir X16 61021")
    tran0.writeAction("slorii X16 X16 12 2724")
    tran0.writeAction("slorii X16 X16 12 2329")
    tran0.writeAction("slorii X16 X16 12 809")
    tran0.writeAction("slorii X16 X16 12 1709")
    tran0.writeAction("movir X17 39078")
    tran0.writeAction("slorii X17 X17 12 342")
    tran0.writeAction("slorii X17 X17 12 1114")
    tran0.writeAction("slorii X17 X17 12 3005")
    tran0.writeAction("slorii X17 X17 12 2218")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
