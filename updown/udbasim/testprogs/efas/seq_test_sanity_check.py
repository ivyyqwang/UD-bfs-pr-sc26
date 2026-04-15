from EFA_v2 import *
def seq_test_sanity_check():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "new_thread": 0}
    tran0 = state.writeTransition("eventCarry", state, state, event_map['new_thread'])
    for i in range(2):
        tran0.writeAction(f"mov_reg2reg X{8+i} X{i+16}")
    tran0.writeAction("add X16 X17 X31")
    tran0.writeAction("sub X16 X17 X30")
    tran0.writeAction("print 'reg states: reg31=%d reg30=%d reg2=%i' X31 X30 X2")
    # can add more actions here, e.g. write to memory so top can check
    tran0.writeAction("yield_terminate")
    return efa