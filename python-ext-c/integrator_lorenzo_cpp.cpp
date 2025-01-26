#include <limits>
#include <vector>

using std::vector;

extern "C" {
    vector<float> e1_integrator_lorenzo_cpp (
            float dt,
            float T,
            float alpha,
            float tau,
            vector<float> spike_times
            ) {

        // This is currently highly unoptimized since we are pushing back at every
        // iteration. Maybe I should reserve directly the number of steps

        spike_times.push_back(std::numeric_limits<float>::max());
        auto t_next_spike = spike_times.begin();
        
        float x = 0;
        vector<float> x_t{0,};

        // Manually compute the integration times I guess
        for (auto t=0.; t += dt; t<T) {
            if (t >= *t_next_spike) {
                x += alpha * (1-x);
                t_next_spike += 1;
            }
            else {x -= x/tau * dt;};

            x_t.push_back(x);
        }
        return x_t;
    }
}
