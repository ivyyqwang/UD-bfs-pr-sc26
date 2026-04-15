from EFA_v2 import *
def mul_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7871379331299923185, -6116469283759308003]
    tran0.writeAction("movir X16 37571")
    tran0.writeAction("slorii X16 X16 12 995")
    tran0.writeAction("slorii X16 X16 12 985")
    tran0.writeAction("slorii X16 X16 12 2114")
    tran0.writeAction("slorii X16 X16 12 2831")
    tran0.writeAction("movir X17 43805")
    tran0.writeAction("slorii X17 X17 12 3833")
    tran0.writeAction("slorii X17 X17 12 1989")
    tran0.writeAction("slorii X17 X17 12 3844")
    tran0.writeAction("slorii X17 X17 12 797")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
