from EFA_v2 import *
def fmul_64_81():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17688404287245799173, 10619575428090014762]
    tran0.writeAction("movir X16 62841")
    tran0.writeAction("slorii X16 X16 12 3423")
    tran0.writeAction("slorii X16 X16 12 2920")
    tran0.writeAction("slorii X16 X16 12 3204")
    tran0.writeAction("slorii X16 X16 12 3845")
    tran0.writeAction("movir X17 37728")
    tran0.writeAction("slorii X17 X17 12 1273")
    tran0.writeAction("slorii X17 X17 12 1600")
    tran0.writeAction("slorii X17 X17 12 3162")
    tran0.writeAction("slorii X17 X17 12 3114")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
