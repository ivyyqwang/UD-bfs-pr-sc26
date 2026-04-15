from EFA_v2 import *
def vdiv_i32_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1948534764, 1110309158, -1027800070, -1445830726, -2017709722, -1464266316, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1058")
    tran0.writeAction("slorii X19 X19 12 3577")
    tran0.writeAction("slorii X19 X19 8 38")
    tran0.writeAction("slorii X19 X19 12 2237")
    tran0.writeAction("slorii X19 X19 12 3000")
    tran0.writeAction("slorii X19 X19 8 20")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2717")
    tran0.writeAction("slorii X17 X17 12 607")
    tran0.writeAction("slorii X17 X17 8 186")
    tran0.writeAction("slorii X17 X17 12 3115")
    tran0.writeAction("slorii X17 X17 12 3331")
    tran0.writeAction("slorii X17 X17 8 250")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2699")
    tran0.writeAction("slorii X18 X18 12 2321")
    tran0.writeAction("slorii X18 X18 8 180")
    tran0.writeAction("slorii X18 X18 12 2171")
    tran0.writeAction("slorii X18 X18 12 3121")
    tran0.writeAction("slorii X18 X18 8 102")
    tran0.writeAction("vdiv.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
