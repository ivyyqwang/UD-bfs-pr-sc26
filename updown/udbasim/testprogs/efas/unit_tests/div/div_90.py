from EFA_v2 import *
def div_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8484542724103328227, -7831206920972320558]
    tran0.writeAction("movir X16 30143")
    tran0.writeAction("slorii X16 X16 12 618")
    tran0.writeAction("slorii X16 X16 12 1935")
    tran0.writeAction("slorii X16 X16 12 3293")
    tran0.writeAction("slorii X16 X16 12 483")
    tran0.writeAction("movir X17 37713")
    tran0.writeAction("slorii X17 X17 12 3948")
    tran0.writeAction("slorii X17 X17 12 3072")
    tran0.writeAction("slorii X17 X17 12 3540")
    tran0.writeAction("slorii X17 X17 12 210")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
