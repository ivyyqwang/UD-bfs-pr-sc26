from EFA_v2 import *
def fmadd_64_70():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6097886872311191375, 9416557382090113328, 10480084821921801729]
    tran0.writeAction("movir X16 21664")
    tran0.writeAction("slorii X16 X16 12 188")
    tran0.writeAction("slorii X16 X16 12 3432")
    tran0.writeAction("slorii X16 X16 12 2565")
    tran0.writeAction("slorii X16 X16 12 1871")
    tran0.writeAction("movir X17 33454")
    tran0.writeAction("slorii X17 X17 12 1360")
    tran0.writeAction("slorii X17 X17 12 3142")
    tran0.writeAction("slorii X17 X17 12 2308")
    tran0.writeAction("slorii X17 X17 12 304")
    tran0.writeAction("movir X18 37232")
    tran0.writeAction("slorii X18 X18 12 3033")
    tran0.writeAction("slorii X18 X18 12 3746")
    tran0.writeAction("slorii X18 X18 12 2506")
    tran0.writeAction("slorii X18 X18 12 1537")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
