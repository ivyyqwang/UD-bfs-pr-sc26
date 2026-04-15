from EFA_v2 import *
def fadd_64_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14289737263609036730, 8481999755368162566]
    tran0.writeAction("movir X16 50767")
    tran0.writeAction("slorii X16 X16 12 1413")
    tran0.writeAction("slorii X16 X16 12 1211")
    tran0.writeAction("slorii X16 X16 12 323")
    tran0.writeAction("slorii X16 X16 12 4026")
    tran0.writeAction("movir X17 30134")
    tran0.writeAction("slorii X17 X17 12 477")
    tran0.writeAction("slorii X17 X17 12 1667")
    tran0.writeAction("slorii X17 X17 12 2742")
    tran0.writeAction("slorii X17 X17 12 1286")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
