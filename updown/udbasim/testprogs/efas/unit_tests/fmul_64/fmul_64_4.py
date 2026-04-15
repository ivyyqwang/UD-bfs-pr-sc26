from EFA_v2 import *
def fmul_64_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17005546920338685298, 14645974767683744323]
    tran0.writeAction("movir X16 60415")
    tran0.writeAction("slorii X16 X16 12 3437")
    tran0.writeAction("slorii X16 X16 12 806")
    tran0.writeAction("slorii X16 X16 12 103")
    tran0.writeAction("slorii X16 X16 12 3442")
    tran0.writeAction("movir X17 52032")
    tran0.writeAction("slorii X17 X17 12 3911")
    tran0.writeAction("slorii X17 X17 12 1049")
    tran0.writeAction("slorii X17 X17 12 507")
    tran0.writeAction("slorii X17 X17 12 579")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
