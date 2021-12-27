# amgen
command line tool for frequent amgen HDL tasks (generate sources, show design)

Usage:
* generate verilog:
    `amgen generate verilog amlib.utils.EdgeToPulse`

* generate RTLIL:
    `amgen generate rtlil amlib.utils.EdgeToPulse`

* generate CXXRTL:
    `amgen generate cxxrtl amlib.utils.EdgeToPulse`

* show yosys RTL representation:
    `amgen show amlib.utils.EdgeToPulse`
    !['amgen show' command](https://github.com/amaranth-community-unofficial/amgen/blob/main/doc/show.png)

* show netlistsvg RTL representation:
    `amgen netlistsvg  amlib.utils.EdgeToPulse`
    !['amgen netlistsvg' command](https://github.com/amaranth-community-unofficial/amgen/blob/main/doc/netlistsvg.png)
