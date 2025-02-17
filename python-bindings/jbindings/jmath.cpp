#include <iostream>
#include "jmath.hpp"

float add(float a, float b) {
  int result = a + b;
  std::cout << a << " + " << b << " = " << result << "\n";
  return result;
}

float subtract(float a, float b) {
  int result = a - b;
  std::cout << a << " - " << b << " = " << result << "\n";
  return result;
}

float multiply(float a, float b) {
  int result = a * b;
  std::cout << a << " * " << b << " = " << result << "\n";
  return result;
}

float divide(float a, float b) {
  int result = a / b;
  std::cout << a << " / " << b << " = " << result << "\n";
  return result;
}
