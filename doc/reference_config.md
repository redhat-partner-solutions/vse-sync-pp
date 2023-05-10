# Configuration File

Post-processing phase input yaml file specification.
A sample can be found [here](./anl_config.yaml).

## dataInputs Section (required)

Two mutually exclusive different input types contemplated: 1) credentials for OCP cluster and 2) local path.

```{ .yaml .annotate }
dataInputs:
  kubeConfigPath: filename
  localPath: file_path
```

## analyzer Section (required)

Analyzer section parameters:

### maxSteady (int, optional)

Maximum allowed steady state duration of the `analisys` in seconds.

```{ .yaml .annotate}
minSteady: 3600  
```

### minSteady (int, optional)

Minimum allowed period duration of the `analisys` in seconds.

```{ .yaml .annotate}
minSteady: 3600  
```

### maskPRTC (string, optional)

The Primary Reference Time Clock class to satisfy. 
Allowed Values: [PRTC-A, PRTC-B]

```{ .yaml .annotate }
maskPRTC: "PRTC-A"
```

### maskClock (string, optional)

The clock class to satisfy. Allowed Values: [Class-A, "Class-B", "Class-C", "Class-D"]

```{ .yaml .annotate }
maskClock: "Class-C"
```

### clockTargets (object, required)

Multiple roles can be specificed for post-processing through `clockTargets` in the config file. The role or set of roles selected determine the data subset to analyze.

```{ .yaml .annotate }
clockTargets:
  - name: "gnss"
  - name: "tgm"
  - name: "tbc"
  - name: "toc"
```

## observability Section (required)

In addition to generating reports from the analisys, we shall support the generation of plots. Two kind of plots could be supported: `local` for visualizing results in your local computer and `remote` for visualizing results in a hub cluster with certain requirements. 

```{ .yaml .annotate }
observability:
  type: "local"
```