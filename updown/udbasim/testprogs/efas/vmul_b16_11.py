from EFA_v2 import *
def vmul_b16_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [46645, 11352, 18225, 58155, 13572, 46393, 34340, 23285, 47655, 7438, 42710, 5504, 11]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3634")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("slorii X19 X19 12 1139")
    tran0.writeAction("slorii X19 X19 4 1")
    tran0.writeAction("slorii X19 X19 12 709")
    tran0.writeAction("slorii X19 X19 4 8")
    tran0.writeAction("slorii X19 X19 12 2915")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1455")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("slorii X17 X17 12 2146")
    tran0.writeAction("slorii X17 X17 4 4")
    tran0.writeAction("slorii X17 X17 12 2899")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("slorii X17 X17 12 848")
    tran0.writeAction("slorii X17 X17 4 4")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 344")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 2669")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("slorii X18 X18 12 464")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("slorii X18 X18 12 2978")
    tran0.writeAction("slorii X18 X18 4 7")
    tran0.writeAction("vmul.b16 X19 X17 X18 11 ")
    tran0.writeAction("yieldt")
    return efa
