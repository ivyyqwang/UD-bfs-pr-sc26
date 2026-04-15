from EFA_v2 import *
def div_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3132885009376168605, 8243640834373249436]
    tran0.writeAction("movir X16 54405")
    tran0.writeAction("slorii X16 X16 12 3098")
    tran0.writeAction("slorii X16 X16 12 3781")
    tran0.writeAction("slorii X16 X16 12 4043")
    tran0.writeAction("slorii X16 X16 12 1379")
    tran0.writeAction("movir X17 29287")
    tran0.writeAction("slorii X17 X17 12 1210")
    tran0.writeAction("slorii X17 X17 12 2436")
    tran0.writeAction("slorii X17 X17 12 2958")
    tran0.writeAction("slorii X17 X17 12 2460")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
