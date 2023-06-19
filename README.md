# vse-sync-pp

The main purpose of this repo is to offer the packages necessary to run the reference implementation of synchronization tests.

## Setup

Installable Python kits, and information about using Python, are available at [python.org](python.org).

1. [Install python >3.10](https://www.python.org/downloads/)
1. [Install pip](https://packaging.python.org/en/latest/guides/installing-using-linux-tools/)
1. Clone the repo
    ```git clone git@github.com:redhat-partner-solutions/vse-sync-pp.git``` 
1. Install required module dependencies
    ```pip3 install pandas pyyaml numpy```
1. Set Python env variable with the location of the new `vse-sync-pp` module files: 
    ```export PYTHONPATH=vse-sync-pp/src```


## Running

### Parse a log file

To see the parsers available:

    python3 -m vse_sync_pp.parse --help

To parse an existing log file:

    python3 -m vse_sync_pp.parse <filename> <parser>

To parse data presented on stdin:

    python3 -m vse_sync_pp.parse - <parser>

To output timestamps relative to the timestamp of the first accepted log line:

    python3 -m vse_sync_pp.parse --relative <filename> <parser>

### Plot unfiltered log data

To see the parsers available:

    python3 -m vse_sync_pp.plot --help

To plot data from existing log file `<filename>` to `<image>`:

    python3 -m vse_sync_pp.plot <filename> <parser> <image>

To plot data presented on stdin:

    python3 -m vse_sync_pp.plot - <parser> <image>

To plot already parsed (canonical) data:

    python3 -m vse_sync_pp.plot --canonical <filename> <parser> <image>

### Analyze unfiltered log data

To see the analyzers available:

    python3 -m vse_sync_pp.analyze --help

To analyze data from existing log file:

    python3 -m vse_sync_pp.analyze <filename> <analyzer>

To analyze data presented on stdin:

    python3 -m vse_sync_pp.analyze - <analyzer>

To analyze already parsed (canonical) data:

    python3 -m vse_sync_pp.analyze --canonical <filename> <analyzer>

## Contributing

### Parsers

Log file parsers are contributed into `src/vse_sync_pp/parsers/`.

Each log file parser must be represented by a separate class that:

* is provided in an appropriate module, with module named by:
    * user space process;
    * kernel module; or,
    * functional area
* is registered in `vse_sync_pp.parse.PARSERS`
* has unit test cases built by class `ParserTestBuilder`
    * (`tests/vse_sync_pp/parsers/test_parser.py`)

### Analyzers

Log file analyzers are contributed into `src/vse_sync_pp/analyzers/`.

Each log file analyzer myst be represented by a separate class that:

* is provided in an appropriate module
* is registered in `vse_sync_pp.analyze.ANALYZERS`
* has unit test cases built by class `AnalyzerTestBuilder`
    * (`tests/vse_sync_pp/analyzers/test_analyzer.py`)
