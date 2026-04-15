from EFA_v2 import *
def fmadd_64_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13956962067033807759, 7590525155211206225, 5131821397953819488]
    tran0.writeAction("movir X16 49585")
    tran0.writeAction("slorii X16 X16 12 368")
    tran0.writeAction("slorii X16 X16 12 3461")
    tran0.writeAction("slorii X16 X16 12 621")
    tran0.writeAction("slorii X16 X16 12 2959")
    tran0.writeAction("movir X17 26966")
    tran0.writeAction("slorii X17 X17 12 3942")
    tran0.writeAction("slorii X17 X17 12 2447")
    tran0.writeAction("slorii X17 X17 12 125")
    tran0.writeAction("slorii X17 X17 12 3665")
    tran0.writeAction("movir X18 18231")
    tran0.writeAction("slorii X18 X18 12 3653")
    tran0.writeAction("slorii X18 X18 12 3891")
    tran0.writeAction("slorii X18 X18 12 3219")
    tran0.writeAction("slorii X18 X18 12 864")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
