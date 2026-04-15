from EFA_v2 import *
def vsqrt_32_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [781965553, 4157252046, 3687652892, 1648456659, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3964")
    tran0.writeAction("slorii X19 X19 12 2721")
    tran0.writeAction("slorii X19 X19 8 206")
    tran0.writeAction("slorii X19 X19 12 745")
    tran0.writeAction("slorii X19 X19 12 3032")
    tran0.writeAction("slorii X19 X19 8 241")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1572")
    tran0.writeAction("slorii X18 X18 12 371")
    tran0.writeAction("slorii X18 X18 8 211")
    tran0.writeAction("slorii X18 X18 12 3516")
    tran0.writeAction("slorii X18 X18 12 3358")
    tran0.writeAction("slorii X18 X18 8 28")
    tran0.writeAction("vsqrt.32 X19 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
