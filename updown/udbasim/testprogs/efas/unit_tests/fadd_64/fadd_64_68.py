from EFA_v2 import *
def fadd_64_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8300492158315408382, 6391676698606116690]
    tran0.writeAction("movir X16 29489")
    tran0.writeAction("slorii X16 X16 12 1114")
    tran0.writeAction("slorii X16 X16 12 989")
    tran0.writeAction("slorii X16 X16 12 1250")
    tran0.writeAction("slorii X16 X16 12 3070")
    tran0.writeAction("movir X17 22707")
    tran0.writeAction("slorii X17 X17 12 3265")
    tran0.writeAction("slorii X17 X17 12 1987")
    tran0.writeAction("slorii X17 X17 12 2289")
    tran0.writeAction("slorii X17 X17 12 3922")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
