from EFA_v2 import *
def srsubii_54():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4118644628877256540, 11, 1275]
    tran0.writeAction("movir X16 14632")
    tran0.writeAction("slorii X16 X16 12 1495")
    tran0.writeAction("slorii X16 X16 12 2028")
    tran0.writeAction("slorii X16 X16 12 1226")
    tran0.writeAction("slorii X16 X16 12 1884")
    tran0.writeAction("srsubii X16 X17 11 1275")
    tran0.writeAction("yieldt")
    return efa
