#include <vector>
#include <random>

#include "protein.h"


#ifndef SIMULATION_H
#define SIMULATION_H

class Simulation {
private:
	int _dendrite_length;

	float _p_influx;
	int _rate_influx;
	float _p_local_synthesis;
	int _rate_local_synthesis;
	float _prot_p_death;

	std::vector<Protein> _bag;

	std::mt19937_64 _prng;
	std::uniform_real_distribution<float> _dist_std_uniform{0.0,1.0};
	std::bernoulli_distribution _dist_coin{0.5};

	void _step();

public:
	Simulation();
	Simulation(
		const int dendrite_length,
		const int prot_per_box,
		const float p_influx,
		const int rate_influx,
		const float p_local_synthesis,
		const int rate_local_synthesis,
		const float prot_p_death,
		const int seed
	);

	void pulse();
	void run_simulation(const int epochs);
	void write_data(const char* path_to_save_data);

};

#endif 
