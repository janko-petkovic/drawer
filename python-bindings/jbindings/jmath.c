#include <stdio.h>
#include "jmath.h"

float add(float a, float b) {
  float result = a+b;
  printf("Add: %f + %f = %f\n", a, b, result);
  return result;
}

float subtract(float a, float b) {
  float result = a-b;
  printf("Subtract: %f - %f = %f\n", a, b, result);
  return result;
}

float multiply(float a, float b) {
  float result = a*b;
  printf("Multiply: %f * %f = %f\n", a, b, result);
  return result;
}

float divide(float a, float b) {
  float result = a/b;
  printf("Divide: %f / %f = %f\n", a, b, result);
  return result;
}
