# vse-sync-pp

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

## Contributing

### Parsers

Log file parsers are contributed into `src/vse_sync_pp/parsers/`.

Each log file parser must be represented by a separate class that...

* is provided in an appropriate module, with module named by:
    * user space process;
    * kernel module; or,
    * functional area
* is registered in `vse_sync_pp.parse.PARSERS`
* has unit test cases built by class `ParserTestBuilder`
    * (`tests/vse_sync_pp/parsers/test_parser.py`)
