from EFA_v2 import *
def hashl_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5698500223400855552, 7628889210780349353, 4734093503593822554, -635771188301304394]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 20245")
    tran0.writeAction("slorii X17 X17 12 572")
    tran0.writeAction("slorii X17 X17 12 736")
    tran0.writeAction("slorii X17 X17 12 1196")
    tran0.writeAction("slorii X17 X17 12 2048")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 27103")
    tran0.writeAction("slorii X17 X17 12 1061")
    tran0.writeAction("slorii X17 X17 12 335")
    tran0.writeAction("slorii X17 X17 12 1527")
    tran0.writeAction("slorii X17 X17 12 937")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 16818")
    tran0.writeAction("slorii X17 X17 12 3599")
    tran0.writeAction("slorii X17 X17 12 1423")
    tran0.writeAction("slorii X17 X17 12 795")
    tran0.writeAction("slorii X17 X17 12 2394")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 63277")
    tran0.writeAction("slorii X17 X17 12 1175")
    tran0.writeAction("slorii X17 X17 12 2306")
    tran0.writeAction("slorii X17 X17 12 3574")
    tran0.writeAction("slorii X17 X17 12 3510")
    tran0.writeAction("hashl X16 X17 3")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
