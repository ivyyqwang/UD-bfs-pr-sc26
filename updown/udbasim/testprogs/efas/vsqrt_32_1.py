from EFA_v2 import *
def vsqrt_32_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4021599431, 2930329609, 1473232672, 3307056803, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2794")
    tran0.writeAction("slorii X19 X19 12 2376")
    tran0.writeAction("slorii X19 X19 8 9")
    tran0.writeAction("slorii X19 X19 12 3835")
    tran0.writeAction("slorii X19 X19 12 1212")
    tran0.writeAction("slorii X19 X19 8 199")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3153")
    tran0.writeAction("slorii X18 X18 12 3502")
    tran0.writeAction("slorii X18 X18 8 163")
    tran0.writeAction("slorii X18 X18 12 1404")
    tran0.writeAction("slorii X18 X18 12 4031")
    tran0.writeAction("slorii X18 X18 8 32")
    tran0.writeAction("vsqrt.32 X19 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
