from EFA_v2 import *
def vdiv_32_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [769730269, 2960558081, 1181169035, 2099902191, 2797422095, 1558470471, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2823")
    tran0.writeAction("slorii X19 X19 12 1672")
    tran0.writeAction("slorii X19 X19 8 1")
    tran0.writeAction("slorii X19 X19 12 734")
    tran0.writeAction("slorii X19 X19 12 294")
    tran0.writeAction("slorii X19 X19 8 221")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2002")
    tran0.writeAction("slorii X17 X17 12 2550")
    tran0.writeAction("slorii X17 X17 8 239")
    tran0.writeAction("slorii X17 X17 12 1126")
    tran0.writeAction("slorii X17 X17 12 1845")
    tran0.writeAction("slorii X17 X17 8 139")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1486")
    tran0.writeAction("slorii X18 X18 12 1119")
    tran0.writeAction("slorii X18 X18 8 71")
    tran0.writeAction("slorii X18 X18 12 2667")
    tran0.writeAction("slorii X18 X18 12 3398")
    tran0.writeAction("slorii X18 X18 8 15")
    tran0.writeAction("vdiv.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
