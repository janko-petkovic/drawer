#include <iostream>
#include <iterator>
#include <ostream>
#include <vector>
#include <fstream>
#include <random>
#include <algorithm>

#include "protein.h"

int main() {
	float p_influx = 1;
	int rate_influx = 2;
	float p_local_synthesis = 0.1;
	int rate_local_synthesis = 1;

	float p_death = .0001;
	int dendrite_length = 300;
	int p_per_box = 100;
	int epochs = 1000;

	
	// Don't touch from here onward
	std::vector<Protein> bag;
	std::vector<Protein> survivor_bag;

	std::mt19937_64 prng(1234);
	std::uniform_real_distribution<float> dist_std_uniform(0,1);
	std::bernoulli_distribution dist_coin(0.5);

	std::ofstream ofs("../output/data.csv", 
					  std::ofstream::out | std::ofstream::trunc);


	// Load the bag with pulsed proteins
	for (int i=0; i < dendrite_length; i++) {
		for (int j=0; j<p_per_box; j++) {
			bag.push_back(Protein{true, i, p_death});
		};
	};

	// Dynamics
	for (int i=0; i<epochs; i++) {
		
		// Decay
		for (auto it = bag.begin(); it != bag.end(); ) {
			it = dist_std_uniform(prng) > it->p_death ?
				it + 1
				: bag.erase(it);
		};

		// Diffuse
		for (auto& p : bag) {
			p.x = (dist_std_uniform(prng) > 0.5) ? 
				std::min(p.x + 1, dendrite_length-1)
				: std::max(p.x - 1, 0);
		};

		// Influx
		if (dist_std_uniform(prng) < p_influx) {
			for (int i=0; i<rate_influx; i++) {
				bag.push_back(Protein{false, 0, p_death});
			};
		}

		// Local translations
		for (int i=0; i<dendrite_length; i++) {
			if (dist_std_uniform(prng) < p_local_synthesis) {
				for (int ii=0; ii<rate_local_synthesis; ii++) {
					bag.push_back(Protein{false, i, p_death});
				}
			}
		}
		
	};

	for (auto& p : bag) {
		ofs << p.x << ',' << p.glowing << '\n';
	};

	ofs.close();
}
