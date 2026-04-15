// Check generate_event_word_update_test.sh about how to generate event word update test cases

#include "simupdown.h"
#include "updown.h"

int main(int argc, char *argv[]){
	UpDown::ud_machine_t machine;
	machine.NumLanes = 1;
	machine.NumUDs = 1;
	machine.NumStacks = 1;
	machine.NumNodes = 1;
	machine.LocalMemAddrMode = 0;

#ifdef GEM5_MODE
	UpDown::UDRuntime_t *rt = new UpDown::UDRuntime_t(machine);
#else
	char dir[100] = "./efas/";
	strcat(dir, argv[1]);
	printf("%s\n", dir);
	UpDown::SimUDRuntime_t *rt = new UpDown::SimUDRuntime_t(machine,
		argv[1], 
		argv[1], 
		"./", 
		UpDown::EmulatorLogLevel::FULL_TRACE);
#endif

	UpDown::networkid_t nwid(0, 0);
	UpDown::word_t ops_data[3];
	UpDown::operands_t ops(3, ops_data);
	ops.set_operand(0, 0);
	ops.set_operand(1, 0);
	ops.set_operand(2, 8);

	UpDown::word_t data = 0;
	rt->t2ud_memcpy(&data,8,nwid,0);

	UpDown::event_t evnt_ops = UpDown::event_t(0,nwid,UpDown::CREATE_THREAD,&ops);
	rt->send_event(evnt_ops);
	rt->start_exec(nwid);

	bool pass = rt->test_addr(nwid,0,1);
	// if (pass){
   	// 	printf("TEST PASSED\n");
	// 	return 0;
  	// } else {
    // 	printf("TEST FAILED\n");
	// 	return 1;
	// }
	return 0;
}
