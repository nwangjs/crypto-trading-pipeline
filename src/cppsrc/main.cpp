#include "five_tick_volume_feature.hpp"
#include "n_trades_feature.hpp"
#include "percent_buy_feature.hpp"
#include "percent_sell_feature.hpp"
#include <iostream>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;
using namespace intproj;

int main()
{
    std::cout << "hello\n";
}

int add(int a, int b)
{
    return a + b;
}

PYBIND11_MODULE(intern, m)
{
    m.def("add", &add, "Adds two numbers");

    py::class_<BaseFeature>(m, "BaseFeature").def("compute_feature", &BaseFeature::compute_feature);

    py::class_<NTradesFeature, BaseFeature>(m, "NTradesFeature")
      .def(py::init<>())
      .def("compute_feature", &NTradesFeature::compute_feature);

    py::class_<PercentBuyFeature, BaseFeature>(m, "PercentBuyFeature")
      .def(py::init<>())
      .def("compute_feature", &PercentBuyFeature::compute_feature);

    py::class_<PercentSellFeature, BaseFeature>(m, "PercentSellFeature")
      .def(py::init<>())
      .def("compute_feature", &PercentSellFeature::compute_feature);

    py::class_<FiveTickVolumeFeature, BaseFeature>(m, "FiveTickVolumeFeature")
      .def(py::init<>())
      .def("compute_feature", &FiveTickVolumeFeature::compute_feature);
}
