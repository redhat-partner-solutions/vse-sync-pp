### SPDX-License-Identifier: GPL-2.0-or-later

"""Requirements specified in ITU-T G.8272/Y.1367"""

REQUIREMENTS = {
    'G.8272/PRTC-A': {
        'maximum-time-interval-error-in-locked-mode/us': {
            (None, 273): lambda t: 0.000275 * t + 0.025,
            (274, None): lambda t: 0.10
        },
        'time-deviation-in-locked-mode/ns': {
            (None, 100): lambda t: 3,
            (101, 1000): lambda t: 0.03 * t,
            (1001, 10000): lambda t: 30
        },
        'time-error-in-locked-mode/ns': 100,
    },
    'G.8272/PRTC-B': {
        'maximum-time-interval-error-in-locked-mode/us': {
            (None, 54.5): lambda t: 0.000275 * t + 0.025,
            (54.5, None): lambda t: 0.04
        },
        'time-deviation-in-locked-mode/ns': {
            (None, 100): lambda t: 1,
            (101, 500): lambda t: 0.01 * t,
            (501, 100000): lambda t: 5
        },
        'time-error-in-locked-mode/ns': 40,
    },
    'workload/RAN': {
        'time-error-in-locked-mode/ns': 100,
        'time-deviation-in-locked-mode/ns': {
            (None, 100000): lambda t: 100
        },
        'maximum-time-interval-error-in-locked-mode/us': {
            (None, 100000): lambda t: 1
        }
    },
}
