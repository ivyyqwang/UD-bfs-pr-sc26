from EFA_v2 import *
def hash_29():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8801934963710910124, 8157153267398492218]
    tran0.writeAction("movir X16 34265")
    tran0.writeAction("slorii X16 X16 12 1004")
    tran0.writeAction("slorii X16 X16 12 2303")
    tran0.writeAction("slorii X16 X16 12 3770")
    tran0.writeAction("slorii X16 X16 12 340")
    tran0.writeAction("movir X17 28980")
    tran0.writeAction("slorii X17 X17 12 122")
    tran0.writeAction("slorii X17 X17 12 3489")
    tran0.writeAction("slorii X17 X17 12 2884")
    tran0.writeAction("slorii X17 X17 12 58")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
