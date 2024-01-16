g++ cpp/main.cpp cpp/simulation.cpp -std=c++20 -O3 -o bin/simulation
echo -en "Running simulation..."
runtime=$((time ./bin/simulation output/data.csv) 2>&1 | grep real)
echo -e "finished!"
echo -e "> Runtime: "$runtime
python analysis.py

