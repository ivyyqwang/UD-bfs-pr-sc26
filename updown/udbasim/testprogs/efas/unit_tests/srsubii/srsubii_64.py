from EFA_v2 import *
def srsubii_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6746728607040992526, 2, 480]
    tran0.writeAction("movir X16 41566")
    tran0.writeAction("slorii X16 X16 12 3297")
    tran0.writeAction("slorii X16 X16 12 989")
    tran0.writeAction("slorii X16 X16 12 1456")
    tran0.writeAction("slorii X16 X16 12 2802")
    tran0.writeAction("srsubii X16 X17 2 480")
    tran0.writeAction("yieldt")
    return efa
