#!/usr/bin/env python3
import os
import sys
import re

from nmigen                  import Signal
from nmigen._toolchain.yosys import *
from nmigen.hdl.ir           import Fragment

import click
import importlib
import inspect
from   inspect import Signature, Parameter

def _show_rtlil_text(rtlil_text: str, *, src_loc_at=0, optimize=False):
    yosys = find_yosys(lambda ver: ver >= (0, 9, 3468))
    yosys_version = yosys.version()

    module_prefix = "module \\"

    modules = [
        m.replace(module_prefix, "") for m in rtlil_text.split('\n')
                                     if m.startswith(module_prefix)]

    script = []
    script.append("read_ilang <<rtlil\n{}\nrtlil".format(rtlil_text))
    script.append("""
        proc_clean
        proc_init
        proc_arst
        proc_mux
        proc_dlatch
        proc_dff
        proc_clean""")

    if optimize:
        script.append("opt")

    if yosys_version >= (0, 9, 3468):
        # Yosys >=0.9+3468 (since commit 128522f1) emits the workaround for the `always @*`
        # initial scheduling issue on its own.
        script.append("delete w:$verilog_initial_trigger")

    for module in modules:
        script.append("show -nobg -long -width -colors 42 " + module)

    return yosys.run(["-q", "-"], "\n".join(script), src_loc_at=1 + src_loc_at)

def do_show(fragment: Fragment, optimize: bool):
    from nmigen.back import rtlil
    rtlil_text = rtlil.convert(fragment)
    return _show_rtlil_text(rtlil_text, src_loc_at=1)

@click.group()
def cli():
    pass

def get_fragment(class_name: str):
    sys.path.append('.')
    parts = class_name.split('.')
    package_name = ".".join(parts[:-1])
    top_name = parts[-1]
    module = importlib.import_module(package_name)
    design_class = module.__dict__[top_name]

    if not inspect.isclass(design_class):
        print(top_name + " is not a class! exiting...")
        sys.exit(1)

    args = []
    kwargs = {}
    signature = inspect.signature(design_class.__init__)
    for parameter in signature.parameters.values():
        if parameter.name == "self":
            continue

        if (parameter.default == Signature.empty):
            val = input(f"parameter {parameter.name} value: ")

            val_type = int
            if parameter.annotation != Parameter.empty:
                val_type = parameter.annotation
            else:
                val_type_str = input(f"parameter {parameter.name} type: ")
                val_type = eval(val_type_str)

            value = val_type(val)
            if parameter.kind == Parameter.KEYWORD_ONLY:
                kwargs[parameter.name] = value
            elif parameter.kind == Parameter.POSITIONAL_ONLY:
                args.append(value)

    design = design_class(*args, **kwargs)
    ports = [member[1] for member in inspect.getmembers(design) if isinstance(member[1], Signal)]
    fragment = Fragment.get(design, None)
    for port in ports:
        dir=None
        if port.name.endswith("_in"):
            dir="i"
        elif port.name.endswith("_out"):
            dir="o"
        else:
            print(f"The name of port '{port.name}' did not end with _in or _out. Assuming inout.")
            dir="io"
        fragment.add_ports([port], dir=dir)

    return [fragment, top_name]

@cli.command()
@click.argument('class_name')
@click.option('--optimize', is_flag=True)
def show(class_name: str, optimize: bool):
    fragment, name = get_fragment(class_name)
    do_show(fragment, optimize)

@cli.group()
def generate():
    pass

def write_to_file(name: str, extension: str, output: str):
    with open(f"{name}.{extension}", 'w') as f:
        f.write(output)

@generate.command()
@click.argument('class_name')
@click.option('--debug', is_flag=True)
def verilog(class_name: str, debug: bool):
    fragment, name = get_fragment(class_name)
    from nmigen.back import verilog
    output = verilog.convert(fragment,  strip_internal_attrs=(not debug))
    write_to_file(name, "v", output)


def generate_rtlil(class_name: str, debug:bool):
    fragment, name = get_fragment(class_name)
    from nmigen.back import rtlil
    contains_attribute = re.compile(r"^\s*attribute (\\src|\\generator)")
    output = rtlil.convert(fragment)
    if not debug:
        lines = output.split('\n')
        lines = [l for l in lines if contains_attribute.match(l) is None]
        output = "\n".join(lines)
    return (name, output)

@generate.command()
@click.argument('class_name')
@click.option('--debug', is_flag=True)
def rtlil(class_name: str, debug:bool):
    name, output = generate_rtlil(class_name=class_name, debug=debug)
    write_to_file(name, "il", output)

@generate.command()
@click.argument('class_name')
def cxxrtl(class_name: str):
    fragment, name = get_fragment(class_name)
    from nmigen.back import cxxrtl
    output = cxxrtl.convert(fragment)
    write_to_file(name, "cpp", output)

@cli.command()
@click.argument('class_name')
@click.option('--debug', is_flag=True)
@click.option('--optimize', is_flag=True)
def netlistsvg(class_name: str, debug: bool, optimize: bool):
    filename, rtlil_text = generate_rtlil(class_name=class_name, debug=debug)

    yosys = find_yosys(lambda ver: ver >= (0, 9, 3468))
    yosys_version = yosys.version()

    script = []
    script.append("read_ilang <<rtlil\n{}\nrtlil".format(rtlil_text))
    script.append("""
        proc_clean
        proc_init
        proc_arst
        proc_mux
        proc_dlatch
        proc_dff
        proc_clean""")

    if optimize:
        script.append("opt")

    if yosys_version >= (0, 9, 3468):
        # Yosys >=0.9+3468 (since commit 128522f1) emits the workaround for the `always @*`
        # initial scheduling issue on its own.
        script.append("delete w:$verilog_initial_trigger")

    netlist_filename = filename + ".json"
    script.append("write_json " + netlist_filename)
    yosys.run(["-q", "-"], "\n".join(script), src_loc_at=1)
    os.system(f"netlistsvg {netlist_filename} -o {filename}.svg")
    os.system(f"xdg-open {filename}.svg")

if __name__ == '__main__':
    cli()
