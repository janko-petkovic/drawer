#include <fstream>
#include <algorithm>
#include <iostream>

#include "simulation.h"

Simulation::Simulation() {} 

Simulation::Simulation(
	const int dendrite_length,
	const int prot_per_box,
	const float p_influx,
	const int rate_influx,
	const float p_local_synthesis,
	const int rate_local_synthesis,
	const float prot_p_death,
	const int seed
):
	_dendrite_length(dendrite_length),
	_p_influx(p_influx),
	_rate_influx(rate_influx),
	_p_local_synthesis(p_local_synthesis),
	_rate_local_synthesis(rate_local_synthesis),
	_prot_p_death(prot_p_death) 
{
	// Seed the rng
	_prng.seed(seed);

	// Load the _bag with proteins
	for (int i=0; i < _dendrite_length; i++) {
		for (int j=0; j<prot_per_box; j++) {
			_bag.push_back(Protein{false, i, prot_p_death});
		};
	};
}

void Simulation::_step() {
	// Decay
	for (auto it = _bag.begin(); it != _bag.end(); ) {
		it = _dist_std_uniform(_prng) > it->p_death ?
			it + 1
			: _bag.erase(it);
	};

	// Diffuse
	for (auto& p : _bag) {
		p.x = (_dist_std_uniform(_prng) > 0.5) ? 
			std::min(p.x + 1, _dendrite_length-1)
			: std::max(p.x - 1, 0);
	};

	// Influx
	if (_dist_std_uniform(_prng) < _p_influx) {
		for (int i=0; i<_rate_influx; i++) {
			_bag.push_back(Protein{false, 0, _prot_p_death});
		};
	}

	// Local translations
	for (int i=0; i<_dendrite_length; i++) {
		if (_dist_std_uniform(_prng) < _p_local_synthesis) {
			for (int ii=0; ii<_rate_local_synthesis; ii++) {
				_bag.push_back(Protein{false, i, _prot_p_death});
			}
		}
	}
}

void Simulation::pulse() {
	for (auto& p : _bag) {
		p.glowing = true;	
	}
}

void Simulation::run_simulation(const int epochs) {
	for (int i=0; i<epochs; i++) {
		_step();
	}
}

void Simulation::write_data(const char* path_to_save_data) {
	std::ofstream ofs{path_to_save_data, std::ofstream::out | std::ofstream::trunc};
	std::cout << "Saving data in: " << path_to_save_data << std::endl;
	for (auto& p : _bag) {
		ofs << p.x << ',' << p.glowing << '\n';
	};
	ofs.close();
}
