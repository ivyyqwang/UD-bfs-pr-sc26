from EFA_v2 import *
def mod_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6260278484704505751, -4768716166971940659]
    tran0.writeAction("movir X16 43295")
    tran0.writeAction("slorii X16 X16 12 94")
    tran0.writeAction("slorii X16 X16 12 756")
    tran0.writeAction("slorii X16 X16 12 685")
    tran0.writeAction("slorii X16 X16 12 105")
    tran0.writeAction("movir X17 48594")
    tran0.writeAction("slorii X17 X17 12 478")
    tran0.writeAction("slorii X17 X17 12 2416")
    tran0.writeAction("slorii X17 X17 12 3994")
    tran0.writeAction("slorii X17 X17 12 205")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
