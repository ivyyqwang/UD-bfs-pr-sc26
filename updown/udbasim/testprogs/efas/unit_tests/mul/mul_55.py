from EFA_v2 import *
def mul_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5573337159649531404, 4068384041476492055]
    tran0.writeAction("movir X16 45735")
    tran0.writeAction("slorii X16 X16 12 2166")
    tran0.writeAction("slorii X16 X16 12 465")
    tran0.writeAction("slorii X16 X16 12 2478")
    tran0.writeAction("slorii X16 X16 12 2548")
    tran0.writeAction("movir X17 14453")
    tran0.writeAction("slorii X17 X17 12 3291")
    tran0.writeAction("slorii X17 X17 12 2818")
    tran0.writeAction("slorii X17 X17 12 304")
    tran0.writeAction("slorii X17 X17 12 2839")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
