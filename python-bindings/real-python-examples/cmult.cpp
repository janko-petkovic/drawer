#include <iostream>

using std::cout;

float cmult(int int_param, float float_param) {
  float return_value = int_param * float_param;

  cout << "\t" << "In cmult: int: " << int_param
       << ", float: " << float_param
       << ", returning: " << return_value << std::endl;

  return return_value;
}
