from EFA_v2 import *
def vsqrt_b16_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [50078, 28975, 58232, 22173, 20816, 26490, 45248, 15948, 6]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1385")
    tran0.writeAction("slorii X19 X19 4 13")
    tran0.writeAction("slorii X19 X19 12 3639")
    tran0.writeAction("slorii X19 X19 4 8")
    tran0.writeAction("slorii X19 X19 12 1810")
    tran0.writeAction("slorii X19 X19 4 15")
    tran0.writeAction("slorii X19 X19 12 3129")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 996")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 2828")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 1655")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 1301")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("vsqrt.b16 X19 X18 6 ")
    tran0.writeAction("yieldt")
    return efa
