g++ cpp/main.cpp -std=c++20 -O3 -o bin/simulation
echo -en "Running simulation..."
runtime=$((time ./bin/simulaiton) 2>&1 | grep real)
echo -e "finished!"
echo -e "> Runtime: "$runtime
python analysis.py

