from EFA_v2 import *
def vgt_32_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3088053058, 4137577659, 955187717, 3832673584, 151640640, 4151230268, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3945")
    tran0.writeAction("slorii X19 X19 12 3692")
    tran0.writeAction("slorii X19 X19 8 187")
    tran0.writeAction("slorii X19 X19 12 2944")
    tran0.writeAction("slorii X19 X19 12 4083")
    tran0.writeAction("slorii X19 X19 8 66")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3655")
    tran0.writeAction("slorii X17 X17 12 501")
    tran0.writeAction("slorii X17 X17 8 48")
    tran0.writeAction("slorii X17 X17 12 910")
    tran0.writeAction("slorii X17 X17 12 3842")
    tran0.writeAction("slorii X17 X17 8 5")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3958")
    tran0.writeAction("slorii X18 X18 12 3775")
    tran0.writeAction("slorii X18 X18 8 60")
    tran0.writeAction("slorii X18 X18 12 144")
    tran0.writeAction("slorii X18 X18 12 2522")
    tran0.writeAction("slorii X18 X18 8 64")
    tran0.writeAction("vgt.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
