# List of Tests
## Summary
This document provides a summary of the tests included in the Test Suite. Each test lists a general overview of what the test does, a link to the test code for that test, and links to additional information when relevant/available.

## List of T-GM Tests

### GNSS_receiver_to_DPLL_PPS_state

This test verifies that a valid 1PPS signal coming from the GNSS receiver arrives at the DPLL of the WPC card based on an input PRTC-class to satisfy.

#### Test Procedure

Gather the DPLL interface in kernel subsystem interface and grep for the two values in PPS DPLL (Status, and Phase offset [ns]) every second. Note that the `PPS_DPLL_OFFSET` value evolves every second so taking only 1 value does not ensure anything (we should capture the evolution in time and plot a graph), the value should be bounded by abs (-30,+30)ns. Note when interpreting the results that the `PPS_DPLL_OFFSET` comes in the order of 10s of picoseconds.

```
PPS_DPLL_STATE := cat /sys/class/net/ens2f0/device/dpll_1_state | awk '{printf $1","}'
PPS_DPLL_OFFSET := `cat /sys/class/net/ens2f0/device/dpll_1_offset | awk '{print $1/100}'`
```

Characterization 1PPS DPLL component, leverage G.8272/Y.1367 to measure uner normal locked operation conditions:

* DPLL Phase Offset time Error: The time error function during a lengty observation interval.

* DPLL Phase Offset constant Time Error (cTE): The constant time error (CTE) is defined as the mean value of the time error function during a lengthy observation interval in accordance with ITU-T G.8273.2/Y.1368: "the time error samples are measured through a moving-average low-pass filter of at least 100 consecutive time error samples. This filter is applied by the test equipment to remove errors caused by timestamp quantization, or any quantization of packet position in the test equipment, before calculating the maximum time error"

* Wander in locked model characterization of 1PPS DPLL Phase Offset. MTIE and TDEV requirements for 1PPS output interfaces are based on the time interval error of the 1PPS signal taken at one sample per second and without any low-pass filtering.
	- DPLL Phase Offset Maximum Time Interval Error (MTIE): The maximum time interval error, abbreviated as MTIE, is a measure of a clock’s maximum time error over a specified time interval.

	- DPLL Phase Offset Time Deviation (TDEV): The time deviation is defined as the time stability of in this case the DPLL Phase offset versus observation interval tau of the measured clock source. As a result, the time deviation becomes a standard deviation type of measurement to represent the signal source’s time instability.

#### Data Gathering/Report

* Gather the values indicated by PPS DPLL including: Current reference, Status, and Phase offset during a minimum of 300s (recommended value is 9600s).

* Plot PPS DPLL phase offset time error evolution over time.
* Plot PPS DPLL phase offset constant time error evolution over time.
* Plot PPS DPLL Phase Offset Maximum Time Interval Error (MTIE) over time.
* Plot PPS DPLL Phase Offset Time Deviation (TDEV) over time.

#### Test Result / Pass and Fail criteria

* Passed:
	1) PPS DPLL status is 3 (`locked_ho_acq`).
 	2) The absolute value of 1PPS DPLL Phase Offset (in ns) satisfies input
PRTC-class.
 	3) The 1PPS DPLL Phase Offset constant time error (in ns) satisfies input
      PRTC-class
 	4) The 1PPS DPLL MTIE satisfies input PRTC-class.
    5) The value of 1PPS DPLL Phase Offset (in ns) satisfies input PRTC-class.

* Failed: 1) and/or 2) and/or 3) and/or 4) and/or 5) are not satisfied
