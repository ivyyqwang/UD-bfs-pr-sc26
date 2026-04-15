from EFA_v2 import *
def fsub_64_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8177806110332704720, 17580192020210463191]
    tran0.writeAction("movir X16 29053")
    tran0.writeAction("slorii X16 X16 12 1653")
    tran0.writeAction("slorii X16 X16 12 1112")
    tran0.writeAction("slorii X16 X16 12 1637")
    tran0.writeAction("slorii X16 X16 12 2000")
    tran0.writeAction("movir X17 62457")
    tran0.writeAction("slorii X17 X17 12 1591")
    tran0.writeAction("slorii X17 X17 12 3999")
    tran0.writeAction("slorii X17 X17 12 3283")
    tran0.writeAction("slorii X17 X17 12 471")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
