// A simple program that computes the square root of a number
#include <cmath>
#include <iostream>
#include <string>

// TODO 11: Include TutorialConfig.h
// This is some major bs since it fucks with the linter my god
#include "TutorialConfig.h"

int main(int argc, char* argv[])
{
  if (argc < 2) {
    std::cout << argv[0] << " Version " << tutorial_VERSION_MAJOR << "."
              << tutorial_VERSION_MINOR << std::endl;
    std::cout << "Usage: " << argv[0] << " number" << std::endl;
    return 1;
  }

  // convert input to double
  double const inputValue = std::stod(argv[1]);

  // calculate square root
  double const outputValue = sqrt(inputValue);
  std::cout << "The square root of " << inputValue << " is " << outputValue
            << std::endl;
  return 0;
}
