#include "jlib.h"
#include <iostream>

JClass::JClass() {};
void JClass::printValue(int i) {std::cout << i << '\n'; }
void JClass::sendDataBuffer(char* ptr) {
	for (int i=0; i<5; i++) {
		std::cout << (int)ptr[i] << '\n';
	}
}
