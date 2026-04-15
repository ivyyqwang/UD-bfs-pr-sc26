from EFA_v2 import *
def vmul_32_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2348622700, 230214765, 3716889240, 1093785933, 158711679, 2802879397, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 219")
    tran0.writeAction("slorii X19 X19 12 2252")
    tran0.writeAction("slorii X19 X19 8 109")
    tran0.writeAction("slorii X19 X19 12 2239")
    tran0.writeAction("slorii X19 X19 12 3363")
    tran0.writeAction("slorii X19 X19 8 108")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1043")
    tran0.writeAction("slorii X17 X17 12 473")
    tran0.writeAction("slorii X17 X17 8 77")
    tran0.writeAction("slorii X17 X17 12 3544")
    tran0.writeAction("slorii X17 X17 12 2874")
    tran0.writeAction("slorii X17 X17 8 152")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2673")
    tran0.writeAction("slorii X18 X18 12 139")
    tran0.writeAction("slorii X18 X18 8 165")
    tran0.writeAction("slorii X18 X18 12 151")
    tran0.writeAction("slorii X18 X18 12 1471")
    tran0.writeAction("slorii X18 X18 8 127")
    tran0.writeAction("vmul.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
