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
	char dir[100] = "../tests/";
	strcat(dir, argv[1]);
	printf("%s\n", dir);
	UpDown::SimUDRuntime_t *rt = new UpDown::SimUDRuntime_t(machine,
		argv[1],
		argv[1], 
		"./", 
		UpDown::EmulatorLogLevel::FULL_TRACE);
#endif

	UpDown::networkid_t nwid(0, 0);
	int num_ops = argc-2;
	UpDown::word_t ops_data[num_ops > 2 ? num_ops : 2];
	UpDown::operands_t ops(num_ops > 2 ? num_ops : 2, ops_data);
	int persistent_operand_value = 8;
	ops.set_operand(0, persistent_operand_value);
	ops.set_operand(1, rand());
	for(int i=0; i < num_ops; i++){
		ops.set_operand(i, atoi(argv[i+2]));
	}

	UpDown::word_t data = 0;
	rt->t2ud_memcpy(&data,8,nwid,0);
	
	UpDown::event_t evnt_ops = UpDown::event_t(0,nwid,UpDown::CREATE_THREAD,&ops);
	rt->send_event(evnt_ops);
	rt->start_exec(nwid);

	uint32_t expected_val = 1;
	if (rt->test_addr(nwid,0,expected_val)){
   		printf("TEST PASSED\n");
		return 0;
  	} else {
    	printf("TEST FAILED\n");
		return 1;
	}
}
