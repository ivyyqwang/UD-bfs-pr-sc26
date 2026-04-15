from EFA_v2 import *
def vsub_32_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [432149192, 864459027, 2080245150, 725338744, 3377481079, 3476289410, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 824")
    tran0.writeAction("slorii X19 X19 12 1689")
    tran0.writeAction("slorii X19 X19 8 19")
    tran0.writeAction("slorii X19 X19 12 412")
    tran0.writeAction("slorii X19 X19 12 530")
    tran0.writeAction("slorii X19 X19 8 200")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 691")
    tran0.writeAction("slorii X17 X17 12 3018")
    tran0.writeAction("slorii X17 X17 8 120")
    tran0.writeAction("slorii X17 X17 12 1983")
    tran0.writeAction("slorii X17 X17 12 3589")
    tran0.writeAction("slorii X17 X17 8 158")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3315")
    tran0.writeAction("slorii X18 X18 12 1015")
    tran0.writeAction("slorii X18 X18 8 130")
    tran0.writeAction("slorii X18 X18 12 3221")
    tran0.writeAction("slorii X18 X18 12 69")
    tran0.writeAction("slorii X18 X18 8 119")
    tran0.writeAction("vsub.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
