from EFA_v2 import *
def srsubii_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [912374991559209900, 10, 956]
    tran0.writeAction("movir X16 3241")
    tran0.writeAction("slorii X16 X16 12 1667")
    tran0.writeAction("slorii X16 X16 12 2185")
    tran0.writeAction("slorii X16 X16 12 3427")
    tran0.writeAction("slorii X16 X16 12 940")
    tran0.writeAction("srsubii X16 X17 10 956")
    tran0.writeAction("yieldt")
    return efa
