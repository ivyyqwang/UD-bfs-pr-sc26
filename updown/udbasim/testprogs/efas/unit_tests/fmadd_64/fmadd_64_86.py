from EFA_v2 import *
def fmadd_64_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10062033985584011868, 14648146139443565734, 12162984403245485061]
    tran0.writeAction("movir X16 35747")
    tran0.writeAction("slorii X16 X16 12 2153")
    tran0.writeAction("slorii X16 X16 12 2388")
    tran0.writeAction("slorii X16 X16 12 2633")
    tran0.writeAction("slorii X16 X16 12 2652")
    tran0.writeAction("movir X17 52040")
    tran0.writeAction("slorii X17 X17 12 2740")
    tran0.writeAction("slorii X17 X17 12 3579")
    tran0.writeAction("slorii X17 X17 12 2225")
    tran0.writeAction("slorii X17 X17 12 1190")
    tran0.writeAction("movir X18 43211")
    tran0.writeAction("slorii X18 X18 12 2461")
    tran0.writeAction("slorii X18 X18 12 3932")
    tran0.writeAction("slorii X18 X18 12 260")
    tran0.writeAction("slorii X18 X18 12 3077")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
