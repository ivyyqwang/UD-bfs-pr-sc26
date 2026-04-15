from EFA_v2 import *
def fmadd_64_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7587804304868628033, 16008792339521750267, 13942570367582302548]
    tran0.writeAction("movir X16 26957")
    tran0.writeAction("slorii X16 X16 12 1213")
    tran0.writeAction("slorii X16 X16 12 56")
    tran0.writeAction("slorii X16 X16 12 3581")
    tran0.writeAction("slorii X16 X16 12 1601")
    tran0.writeAction("movir X17 56874")
    tran0.writeAction("slorii X17 X17 12 2685")
    tran0.writeAction("slorii X17 X17 12 136")
    tran0.writeAction("slorii X17 X17 12 772")
    tran0.writeAction("slorii X17 X17 12 1275")
    tran0.writeAction("movir X18 49533")
    tran0.writeAction("slorii X18 X18 12 3934")
    tran0.writeAction("slorii X18 X18 12 223")
    tran0.writeAction("slorii X18 X18 12 2583")
    tran0.writeAction("slorii X18 X18 12 340")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
