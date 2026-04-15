from EFA_v2 import *
def vmul_32_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3868593062, 832989067, 3558916237, 1557715370, 1044297174, 960861588, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 794")
    tran0.writeAction("slorii X19 X19 12 1639")
    tran0.writeAction("slorii X19 X19 8 139")
    tran0.writeAction("slorii X19 X19 12 3689")
    tran0.writeAction("slorii X19 X19 12 1547")
    tran0.writeAction("slorii X19 X19 8 166")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1485")
    tran0.writeAction("slorii X17 X17 12 2265")
    tran0.writeAction("slorii X17 X17 8 170")
    tran0.writeAction("slorii X17 X17 12 3394")
    tran0.writeAction("slorii X17 X17 12 192")
    tran0.writeAction("slorii X17 X17 8 141")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 916")
    tran0.writeAction("slorii X18 X18 12 1429")
    tran0.writeAction("slorii X18 X18 8 148")
    tran0.writeAction("slorii X18 X18 12 995")
    tran0.writeAction("slorii X18 X18 12 3765")
    tran0.writeAction("slorii X18 X18 8 214")
    tran0.writeAction("vmul.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
