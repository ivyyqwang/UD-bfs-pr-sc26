from EFA_v2 import *
def div_32():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8599760334576092954, -7481658142507080275]
    tran0.writeAction("movir X16 30552")
    tran0.writeAction("slorii X16 X16 12 1991")
    tran0.writeAction("slorii X16 X16 12 1527")
    tran0.writeAction("slorii X16 X16 12 3696")
    tran0.writeAction("slorii X16 X16 12 1818")
    tran0.writeAction("movir X17 38955")
    tran0.writeAction("slorii X17 X17 12 3320")
    tran0.writeAction("slorii X17 X17 12 3860")
    tran0.writeAction("slorii X17 X17 12 3918")
    tran0.writeAction("slorii X17 X17 12 1453")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
