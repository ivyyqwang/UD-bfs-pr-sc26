from EFA_v2 import *
def hash_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8223026036456779657, -4781705957800228452]
    tran0.writeAction("movir X16 36321")
    tran0.writeAction("slorii X16 X16 12 3862")
    tran0.writeAction("slorii X16 X16 12 806")
    tran0.writeAction("slorii X16 X16 12 841")
    tran0.writeAction("slorii X16 X16 12 119")
    tran0.writeAction("movir X17 48547")
    tran0.writeAction("slorii X17 X17 12 3964")
    tran0.writeAction("slorii X17 X17 12 1044")
    tran0.writeAction("slorii X17 X17 12 3884")
    tran0.writeAction("slorii X17 X17 12 2460")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
