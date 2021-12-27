# an-amaranth-tool
unofficial command line tool for frequent amaranth HDL tasks (generate sources, show design)

Usage:
* generate verilog:
    `amaranth generate verilog amaranth_library.utils.EdgeToPulse`

* generate RTLIL:
    `amaranth generate rtlil amaranth_library.utils.EdgeToPulse`

* generate CXXRTL:
    `amaranth generate cxxrtl amaranth_library.utils.EdgeToPulse`

* show yosys RTL representation:
    `amaranth show amaranth_library.utils.EdgeToPulse`
    !['amaranth show' command](https://github.com/hansfbaier/an-amaranth-tool/blob/main/doc/show.png)

* show netlistsvg RTL representation:
    `amaranth netlistsvg  amaranth_library.utils.EdgeToPulse`
    !['amaranth netlistsvg' command](https://github.com/hansfbaier/an-amaranth-tool/blob/main/doc/netlistsvg.png)
