#include "simulation.h"

int main(int argc, char* argv[]) {
	Simulation simulation(300,100,1,2,0.1,1,0.001,1234);
	simulation.pulse();
	simulation.run_simulation(10);
	simulation.write_data(argv[1]);
}
