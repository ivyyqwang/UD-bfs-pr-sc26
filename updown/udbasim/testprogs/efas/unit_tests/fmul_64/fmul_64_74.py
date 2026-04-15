from EFA_v2 import *
def fmul_64_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7030045258812742207, 18334458702636098004]
    tran0.writeAction("movir X16 24975")
    tran0.writeAction("slorii X16 X16 12 3022")
    tran0.writeAction("slorii X16 X16 12 2694")
    tran0.writeAction("slorii X16 X16 12 1853")
    tran0.writeAction("slorii X16 X16 12 2623")
    tran0.writeAction("movir X17 65137")
    tran0.writeAction("slorii X17 X17 12 336")
    tran0.writeAction("slorii X17 X17 12 3271")
    tran0.writeAction("slorii X17 X17 12 2842")
    tran0.writeAction("slorii X17 X17 12 468")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
