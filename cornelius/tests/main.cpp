#include <cstdlib>
#include <random>
#include <iostream>
#include <chrono>
#include <ext/random>

int main() {
	std::mt19937_64 rng(1234);
	// __gnu_cxx::sfmt19937 rng(1234);
	std::uniform_real_distribution<double> uni(0,1);
	std::bernoulli_distribution bern(0.5);

	auto start = std::chrono::high_resolution_clock::now();
	for (auto i=0; i<10000000; i++) { 
		uni(rng);
		// bern(rng);
		// rng();
	}
	auto stop = std::chrono::high_resolution_clock::now();

	auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);

	std::cout << "Marsenne execution time: "
			  << duration.count() << " us"
			  << std::endl;

	start = std::chrono::high_resolution_clock::now();
	for (auto i=0; i<10000000; i++) { 
		std::rand();
	}
	stop = std::chrono::high_resolution_clock::now();

	duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);

	std::cout << "Rand execution time: "
			  << duration.count() << " us"
			  << std::endl;
}
