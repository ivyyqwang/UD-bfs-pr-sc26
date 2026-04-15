from EFA_v2 import *
def fadd_64_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17520484100664915752, 11889307833536669026]
    tran0.writeAction("movir X16 62245")
    tran0.writeAction("slorii X16 X16 12 1079")
    tran0.writeAction("slorii X16 X16 12 1609")
    tran0.writeAction("slorii X16 X16 12 47")
    tran0.writeAction("slorii X16 X16 12 1832")
    tran0.writeAction("movir X17 42239")
    tran0.writeAction("slorii X17 X17 12 1255")
    tran0.writeAction("slorii X17 X17 12 2939")
    tran0.writeAction("slorii X17 X17 12 910")
    tran0.writeAction("slorii X17 X17 12 1378")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
