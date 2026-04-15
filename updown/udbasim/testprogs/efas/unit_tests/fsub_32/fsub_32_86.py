from EFA_v2 import *
def fsub_32_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4196878465, 3318570352]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 250")
    tran0.writeAction("slorii X16 X16 12 628")
    tran0.writeAction("slorii X16 X16 12 2177")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 197")
    tran0.writeAction("slorii X17 X17 12 3285")
    tran0.writeAction("slorii X17 X17 12 3440")
    tran0.writeAction("fsub.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
