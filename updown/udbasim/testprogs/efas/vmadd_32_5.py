from EFA_v2 import *
def vmadd_32_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3323446856, 248455410, 3820990142, 3015356824, 2174754574, 2041223753, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 236")
    tran0.writeAction("slorii X19 X19 12 3872")
    tran0.writeAction("slorii X19 X19 8 242")
    tran0.writeAction("slorii X19 X19 12 3169")
    tran0.writeAction("slorii X19 X19 12 1990")
    tran0.writeAction("slorii X19 X19 8 72")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2875")
    tran0.writeAction("slorii X17 X17 12 2737")
    tran0.writeAction("slorii X17 X17 8 152")
    tran0.writeAction("slorii X17 X17 12 3643")
    tran0.writeAction("slorii X17 X17 12 4014")
    tran0.writeAction("slorii X17 X17 8 190")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1946")
    tran0.writeAction("slorii X18 X18 12 2714")
    tran0.writeAction("slorii X18 X18 8 73")
    tran0.writeAction("slorii X18 X18 12 2074")
    tran0.writeAction("slorii X18 X18 12 31")
    tran0.writeAction("slorii X18 X18 8 14")
    tran0.writeAction("vmadd.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
