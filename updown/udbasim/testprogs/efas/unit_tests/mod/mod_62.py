from EFA_v2 import *
def mod_62():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4261376058495114703, -3148115783833647298]
    tran0.writeAction("movir X16 50396")
    tran0.writeAction("slorii X16 X16 12 2256")
    tran0.writeAction("slorii X16 X16 12 3443")
    tran0.writeAction("slorii X16 X16 12 182")
    tran0.writeAction("slorii X16 X16 12 561")
    tran0.writeAction("movir X17 54351")
    tran0.writeAction("slorii X17 X17 12 2645")
    tran0.writeAction("slorii X17 X17 12 4032")
    tran0.writeAction("slorii X17 X17 12 3256")
    tran0.writeAction("slorii X17 X17 12 1854")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
