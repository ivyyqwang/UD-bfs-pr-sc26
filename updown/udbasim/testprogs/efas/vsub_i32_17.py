from EFA_v2 import *
def vsub_i32_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1834896757, -804529303, -1028858637, -642121475, 761681432, -157078865, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3328")
    tran0.writeAction("slorii X19 X19 12 3035")
    tran0.writeAction("slorii X19 X19 8 105")
    tran0.writeAction("slorii X19 X19 12 2346")
    tran0.writeAction("slorii X19 X19 12 434")
    tran0.writeAction("slorii X19 X19 8 139")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3483")
    tran0.writeAction("slorii X17 X17 12 2560")
    tran0.writeAction("slorii X17 X17 8 253")
    tran0.writeAction("slorii X17 X17 12 3114")
    tran0.writeAction("slorii X17 X17 12 3292")
    tran0.writeAction("slorii X17 X17 8 243")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3946")
    tran0.writeAction("slorii X18 X18 12 810")
    tran0.writeAction("slorii X18 X18 8 175")
    tran0.writeAction("slorii X18 X18 12 726")
    tran0.writeAction("slorii X18 X18 12 1622")
    tran0.writeAction("slorii X18 X18 8 24")
    tran0.writeAction("vsub.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
