from EFA_v2 import *
def vsub_32_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3928980009, 2339042123, 3267429284, 561270258, 3896634376, 1507899450, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2230")
    tran0.writeAction("slorii X19 X19 12 2803")
    tran0.writeAction("slorii X19 X19 8 75")
    tran0.writeAction("slorii X19 X19 12 3746")
    tran0.writeAction("slorii X19 X19 12 3962")
    tran0.writeAction("slorii X19 X19 8 41")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 535")
    tran0.writeAction("slorii X17 X17 12 1101")
    tran0.writeAction("slorii X17 X17 8 242")
    tran0.writeAction("slorii X17 X17 12 3116")
    tran0.writeAction("slorii X17 X17 12 259")
    tran0.writeAction("slorii X17 X17 8 164")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1438")
    tran0.writeAction("slorii X18 X18 12 184")
    tran0.writeAction("slorii X18 X18 8 58")
    tran0.writeAction("slorii X18 X18 12 3716")
    tran0.writeAction("slorii X18 X18 12 492")
    tran0.writeAction("slorii X18 X18 8 8")
    tran0.writeAction("vsub.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
