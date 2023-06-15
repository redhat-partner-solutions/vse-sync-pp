# vse-sync-pp

## Running

### Filter collector data from file 

To see the collector filters available:

    python3 -m vse_sync_pp.filter --help

To filter a collector from file:

    python3 -m vse_sync_pp.filter <filename> <filter>

To filter a collector presented on stdin:

    python3 -m vse_sync_pp.filter - <filter>

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
