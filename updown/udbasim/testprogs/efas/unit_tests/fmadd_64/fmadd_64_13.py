from EFA_v2 import *
def fmadd_64_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5251992195803639934, 1997918095775612204, 6699255512974518785]
    tran0.writeAction("movir X16 18658")
    tran0.writeAction("slorii X16 X16 12 3377")
    tran0.writeAction("slorii X16 X16 12 873")
    tran0.writeAction("slorii X16 X16 12 4095")
    tran0.writeAction("slorii X16 X16 12 126")
    tran0.writeAction("movir X17 7098")
    tran0.writeAction("slorii X17 X17 12 126")
    tran0.writeAction("slorii X17 X17 12 3125")
    tran0.writeAction("slorii X17 X17 12 123")
    tran0.writeAction("slorii X17 X17 12 3372")
    tran0.writeAction("movir X18 23800")
    tran0.writeAction("slorii X18 X18 12 2198")
    tran0.writeAction("slorii X18 X18 12 1302")
    tran0.writeAction("slorii X18 X18 12 1734")
    tran0.writeAction("slorii X18 X18 12 2561")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
