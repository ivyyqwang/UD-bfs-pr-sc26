from EFA_v2 import *
def vdiv_32_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [627887663, 3644376459, 2392164875, 4146946417, 1737169449, 427802265, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3475")
    tran0.writeAction("slorii X19 X19 12 2245")
    tran0.writeAction("slorii X19 X19 8 139")
    tran0.writeAction("slorii X19 X19 12 598")
    tran0.writeAction("slorii X19 X19 12 3278")
    tran0.writeAction("slorii X19 X19 8 47")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3954")
    tran0.writeAction("slorii X17 X17 12 3425")
    tran0.writeAction("slorii X17 X17 8 113")
    tran0.writeAction("slorii X17 X17 12 2281")
    tran0.writeAction("slorii X17 X17 12 1418")
    tran0.writeAction("slorii X17 X17 8 11")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 407")
    tran0.writeAction("slorii X18 X18 12 4030")
    tran0.writeAction("slorii X18 X18 8 153")
    tran0.writeAction("slorii X18 X18 12 1656")
    tran0.writeAction("slorii X18 X18 12 2842")
    tran0.writeAction("slorii X18 X18 8 41")
    tran0.writeAction("vdiv.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
