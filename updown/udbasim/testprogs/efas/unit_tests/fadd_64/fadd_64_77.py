from EFA_v2 import *
def fadd_64_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12715801475396949996, 4081233300546297156]
    tran0.writeAction("movir X16 45175")
    tran0.writeAction("slorii X16 X16 12 2465")
    tran0.writeAction("slorii X16 X16 12 535")
    tran0.writeAction("slorii X16 X16 12 1733")
    tran0.writeAction("slorii X16 X16 12 2028")
    tran0.writeAction("movir X17 14499")
    tran0.writeAction("slorii X17 X17 12 1857")
    tran0.writeAction("slorii X17 X17 12 68")
    tran0.writeAction("slorii X17 X17 12 2281")
    tran0.writeAction("slorii X17 X17 12 3396")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
