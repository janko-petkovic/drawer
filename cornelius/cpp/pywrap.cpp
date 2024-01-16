#include <pybind11/pybind11.h>
#include "simulation.h"

namespace py = pybind11;
constexpr auto byref = py::return_value_policy::reference_internal;


PYBIND11_MODULE(CCRNLS955, m) {
	m.doc() = "The python simulator module";

	py::class_<Simulation>(m, "Simulation")
	.def(py::init<int, int, float, int, float, int, float, int>())
	.def("pulse", &Simulation::pulse, py::call_guard<py::gil_scoped_release>())
	.def("run_simulation", &Simulation::run_simulation, py::call_guard<py::gil_scoped_release>())
	.def("write_data", &Simulation::write_data, py::call_guard<py::gil_scoped_release>())
	;
}
