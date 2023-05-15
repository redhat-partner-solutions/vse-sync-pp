# Execution

## Common Example Commands


### Parse Data from csv file

```
env PYTHONPATH=src python3 -m vse_sync_pp.parse <csv_file> dpll/phase-offset
```

### All-in-one parse and analyze data from csv file

```
env PYTHONPATH=src python3 -m vse_sync_pp.analyze <csv_file> --parse dpll/phase-offset ppsdpll/phase-offset-time-error out
```

### All-in-one parse and analyze from csv input file read from STDIN

```
cat dpll_gnns_time_only.csv | env PYTHONPATH=src python3 -m vse_sync_pp.analyze - --parse dpll/phase-offset ppsdpll/phase-offset-time-error out
```

### Parse from CSV input file. Analyze from parsed data in canonical data format read from STDIN 

```
env PYTHONPATH=src python3 -m vse_sync_pp.parse <csv_file> dpll/phase-offset | env PYTHONPATH=src python3 -m vse_sync_pp.analyze -c - ppsdpll/phase-offset-time-error terror
```
