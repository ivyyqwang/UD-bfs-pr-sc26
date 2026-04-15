from EFA_v2 import *
def fmadd_64_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18071490122766328643, 15941215974853976892, 15196290032525469128]
    tran0.writeAction("movir X16 64202")
    tran0.writeAction("slorii X16 X16 12 3400")
    tran0.writeAction("slorii X16 X16 12 1297")
    tran0.writeAction("slorii X16 X16 12 1914")
    tran0.writeAction("slorii X16 X16 12 835")
    tran0.writeAction("movir X17 56634")
    tran0.writeAction("slorii X17 X17 12 2359")
    tran0.writeAction("slorii X17 X17 12 2060")
    tran0.writeAction("slorii X17 X17 12 3906")
    tran0.writeAction("slorii X17 X17 12 828")
    tran0.writeAction("movir X18 53988")
    tran0.writeAction("slorii X18 X18 12 276")
    tran0.writeAction("slorii X18 X18 12 1388")
    tran0.writeAction("slorii X18 X18 12 2006")
    tran0.writeAction("slorii X18 X18 12 1480")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
