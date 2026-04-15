from EFA_v2 import *
def fmul_64_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1876620913131125313, 16374915656383612761]
    tran0.writeAction("movir X16 6667")
    tran0.writeAction("slorii X16 X16 12 396")
    tran0.writeAction("slorii X16 X16 12 1817")
    tran0.writeAction("slorii X16 X16 12 1023")
    tran0.writeAction("slorii X16 X16 12 2625")
    tran0.writeAction("movir X17 58175")
    tran0.writeAction("slorii X17 X17 12 1584")
    tran0.writeAction("slorii X17 X17 12 2061")
    tran0.writeAction("slorii X17 X17 12 2980")
    tran0.writeAction("slorii X17 X17 12 1881")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
