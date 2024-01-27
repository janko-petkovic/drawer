#include <iostream>
#include "h1.h"
#include "h2.h"

int main() {
	jlib::FirstItem fi(2);
	std::cout << fi.get_i() << '\n';
	jlib::SecondItem si(5);
	std::cout << si.get_i() << '\n';
	return 0;
}
