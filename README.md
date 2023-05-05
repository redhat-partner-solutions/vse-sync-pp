# vse-sync-pp

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
