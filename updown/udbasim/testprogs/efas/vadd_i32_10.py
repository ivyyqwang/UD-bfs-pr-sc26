from EFA_v2 import *
def vadd_i32_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-812480, -1191386828, 1493101797, 1532241362, 1279288252, 1692331301, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2959")
    tran0.writeAction("slorii X19 X19 12 3297")
    tran0.writeAction("slorii X19 X19 8 52")
    tran0.writeAction("slorii X19 X19 12 4095")
    tran0.writeAction("slorii X19 X19 12 922")
    tran0.writeAction("slorii X19 X19 8 64")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1461")
    tran0.writeAction("slorii X17 X17 12 1061")
    tran0.writeAction("slorii X17 X17 8 210")
    tran0.writeAction("slorii X17 X17 12 1423")
    tran0.writeAction("slorii X17 X17 12 3820")
    tran0.writeAction("slorii X17 X17 8 229")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1613")
    tran0.writeAction("slorii X18 X18 12 3821")
    tran0.writeAction("slorii X18 X18 8 37")
    tran0.writeAction("slorii X18 X18 12 1220")
    tran0.writeAction("slorii X18 X18 12 99")
    tran0.writeAction("slorii X18 X18 8 188")
    tran0.writeAction("vadd.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
