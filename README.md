# nmigen-tool
command line tool for frequent nmigen tasks (generate sources, show design)

Usage:
* generate verilog:
    `nmigen generate verilog nmigen_library.utils.EdgeToPulse`

* generate RTLIL:
    `nmigen generate rtlil nmigen_library.utils.EdgeToPulse`

* generate CXXRTL:
    `nmigen generate cxxrtl nmigen_library.utils.EdgeToPulse`

* show yosys RTL representation:
    `nmigen show nmigen_library.utils.EdgeToPulse`
    !['nmigen show' command](https://github.com/hansfbaier/nmigen-tool/blob/main/doc/show.png)

* show netlistsvg RTL representation:
    `nmigen netlistsvg  nmigen_library.utils.EdgeToPulse`
    !['nmigen netlistsvg' command](https://github.com/hansfbaier/nmigen-tool/blob/main/doc/netlistsvg.png)
