### SPDX-License-Identifier: GPL-2.0-or-later

"""Test cases for vse_sync_pp.analyzers.pmc"""

from unittest import TestCase
from collections import namedtuple
from decimal import Decimal

from vse_sync_pp.analyzers.pmc import ClockStateAnalyzer

from .test_analyzer import AnalyzerTestBuilder

CLOCK_CLASS = namedtuple('CLOCK_CLASS', ('timestamp', 'clock_class'))


class TestClockStateAnalyzer(TestCase, metaclass=AnalyzerTestBuilder):
    """Test cases for vse_sync_pp.analyzers.pmc.ClockStateAnalyzer"""
    constructor = ClockStateAnalyzer
    id_ = 'phc/gm-settings'
    parser = 'phc/gm-settings'
    expect = (
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'min-test-duration/s': 1,
            },
            'rows': (),
            'result': False,
            'reason': "no data",
            'analysis': {},
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'min-test-duration/s': 1,
            },
            'rows': (
                CLOCK_CLASS(Decimal('0'), 248),
                CLOCK_CLASS(Decimal('1'), 12),
            ),
            'result': False,
            'reason': "wrong clock class 12",
            'analysis': {
                "duration": 1,
                "clock_class_count": {
                    "FREERUN": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "LOCKED": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_IN_SPEC": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC1": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC2": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC3": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    }
                },
                "total_transitions": 1
            }
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'min-test-duration/s': 1,
            },
            'rows': (
                CLOCK_CLASS(Decimal(0), 248),
                # wrong state transition
                CLOCK_CLASS(Decimal(1), 7),
            ),
            'result': False,
            'reason': "illegal state transition",
            'analysis': {
                "duration": 1,
                "clock_class_count": {
                    "FREERUN": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 1,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "LOCKED": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_IN_SPEC": {
                        "count": 1,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC1": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC2": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC3": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    }
                },
                "total_transitions": 1
            }
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'min-test-duration/s': 1,
            },
            'rows': (
                CLOCK_CLASS(Decimal(0), 248),
                # wrong state transition
                CLOCK_CLASS(Decimal(1), 140),
            ),
            'result': False,
            'reason': "illegal state transition",
            'analysis': {
                "duration": 1,
                "clock_class_count": {
                    "FREERUN": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 1,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "LOCKED": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_IN_SPEC": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC1": {
                        "count": 1,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC2": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC3": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    }
                },
                "total_transitions": 1
            }
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'min-test-duration/s': 1,
            },
            'rows': (
                CLOCK_CLASS(Decimal(0), 248),
                # wrong state transition
                CLOCK_CLASS(Decimal(1), 150),
            ),
            'result': False,
            'reason': "illegal state transition",
            'analysis': {
                "duration": 1,
                "clock_class_count": {
                    "FREERUN": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 1,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "LOCKED": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_IN_SPEC": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC1": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC2": {
                        "count": 1,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC3": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    }
                },
                "total_transitions": 1
            }
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'min-test-duration/s': 1,
            },
            'rows': (
                CLOCK_CLASS(Decimal(0), 248),
                # wrong state transition
                CLOCK_CLASS(Decimal(1), 160),
            ),
            'result': False,
            'reason': "illegal state transition",
            'analysis': {
                "duration": 1,
                "clock_class_count": {
                    "FREERUN": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 1
                        }
                    },
                    "LOCKED": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_IN_SPEC": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC1": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC2": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC3": {
                        "count": 1,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    }
                },
                "total_transitions": 1
            }
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'min-test-duration/s': 1,
            },
            'rows': (
                CLOCK_CLASS(Decimal(0), 6),
                # wrong state transition
                CLOCK_CLASS(Decimal(1), 248),
            ),
            'result': False,
            'reason': "illegal state transition",
            'analysis': {
                "duration": 1,
                "clock_class_count": {
                    "FREERUN": {
                        "count": 1,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "LOCKED": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 1,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_IN_SPEC": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC1": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC2": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC3": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    }
                },
                "total_transitions": 1
            }
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'min-test-duration/s': 1,
            },
            'rows': (
                CLOCK_CLASS(Decimal(0), 6),
                # wrong state transition
                CLOCK_CLASS(Decimal(1), 140),
            ),
            'result': False,
            'reason': "illegal state transition",
            'analysis': {
                "duration": 1,
                "clock_class_count": {
                    "FREERUN": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "LOCKED": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 1,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_IN_SPEC": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC1": {
                        "count": 1,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC2": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC3": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    }
                },
                "total_transitions": 1
            }
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'min-test-duration/s': 1,
            },
            'rows': (
                CLOCK_CLASS(Decimal(0), 6),
                # wrong state transition
                CLOCK_CLASS(Decimal(1), 150),
            ),
            'result': False,
            'reason': "illegal state transition",
            'analysis': {
                "duration": 1,
                "clock_class_count": {
                    "FREERUN": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "LOCKED": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 1,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_IN_SPEC": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC1": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC2": {
                        "count": 1,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC3": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    }
                },
                "total_transitions": 1
            }
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'min-test-duration/s': 1,
            },
            'rows': (
                CLOCK_CLASS(Decimal(0), 6),
                # wrong state transition
                CLOCK_CLASS(Decimal(1), 160),
            ),
            'result': False,
            'reason': "illegal state transition",
            'analysis': {
                "duration": 1,
                "clock_class_count": {
                    "FREERUN": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "LOCKED": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 1
                        }
                    },
                    "HOLDOVER_IN_SPEC": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC1": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC2": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC3": {
                        "count": 1,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    }
                },
                "total_transitions": 1
            }
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'min-test-duration/s': 1,
            },
            'rows': (
                CLOCK_CLASS(Decimal(0), 7),
                # wrong state transition
                CLOCK_CLASS(Decimal(1), 248),
            ),
            'result': False,
            'reason': "illegal state transition",
            'analysis': {
                "duration": 1,
                "clock_class_count": {
                    "FREERUN": {
                        "count": 1,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "LOCKED": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_IN_SPEC": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 1,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC1": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC2": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC3": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    }
                },
                "total_transitions": 1
            }
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'min-test-duration/s': 1,
            },
            'rows': (
                CLOCK_CLASS(Decimal(0), 140),
                # wrong state transition
                CLOCK_CLASS(Decimal(1), 248),
            ),
            'result': False,
            'reason': "illegal state transition",
            'analysis': {
                "duration": 1,
                "clock_class_count": {
                    "FREERUN": {
                        "count": 1,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "LOCKED": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_IN_SPEC": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC1": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 1,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC2": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC3": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    }
                },
                "total_transitions": 1
            }
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'min-test-duration/s': 1,
            },
            'rows': (
                CLOCK_CLASS(Decimal(0), 150),
                # wrong state transition
                CLOCK_CLASS(Decimal(1), 248),
            ),
            'result': False,
            'reason': "illegal state transition",
            'analysis': {
                "duration": 1,
                "clock_class_count": {
                    "FREERUN": {
                        "count": 1,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "LOCKED": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_IN_SPEC": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC1": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC2": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 1,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC3": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    }
                },
                "total_transitions": 1
            }
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'min-test-duration/s': 1,
            },
            'rows': (
                CLOCK_CLASS(Decimal(0), 160),
                # wrong state transition
                CLOCK_CLASS(Decimal(1), 248),
            ),
            'result': False,
            'reason': "illegal state transition",
            'analysis': {
                "duration": 1,
                "clock_class_count": {
                    "FREERUN": {
                        "count": 1,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "LOCKED": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_IN_SPEC": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC1": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC2": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC3": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 1,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    }
                },
                "total_transitions": 1
            }
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'min-test-duration/s': 1,
            },
            'rows': (
                CLOCK_CLASS(Decimal(0), 140),
                # wrong state transition
                CLOCK_CLASS(Decimal(1), 7),
            ),
            'result': False,
            'reason': "illegal state transition",
            'analysis': {
                "duration": 1,
                "clock_class_count": {
                    "FREERUN": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "LOCKED": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_IN_SPEC": {
                        "count": 1,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC1": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 1,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC2": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC3": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    }
                },
                "total_transitions": 1
            }
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'min-test-duration/s': 1,
            },
            'rows': (
                CLOCK_CLASS(Decimal(0), 150),
                # wrong state transition
                CLOCK_CLASS(Decimal(1), 7),
            ),
            'result': False,
            'reason': "illegal state transition",
            'analysis': {
                "duration": 1,
                "clock_class_count": {
                    "FREERUN": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "LOCKED": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_IN_SPEC": {
                        "count": 1,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC1": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC2": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 1,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC3": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    }
                },
                "total_transitions": 1
            }
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'min-test-duration/s': 1,
            },
            'rows': (
                CLOCK_CLASS(Decimal(0), 160),
                # wrong state transition
                CLOCK_CLASS(Decimal(1), 7),
            ),
            'result': False,
            'reason': "illegal state transition",
            'analysis': {
                "duration": 1,
                "clock_class_count": {
                    "FREERUN": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "LOCKED": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_IN_SPEC": {
                        "count": 1,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC1": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC2": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC3": {
                        "count": 0,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 1,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    }
                },
                "total_transitions": 1
            }
        },
        {
            'requirements': 'G.8272/PRTC-B',
            'parameters': {
                'min-test-duration/s': 1,
            },
            'rows': (
                CLOCK_CLASS(Decimal(0), 248),
                CLOCK_CLASS(Decimal(1), 248),
                CLOCK_CLASS(Decimal(2), 6),
                CLOCK_CLASS(Decimal(3), 7),
                CLOCK_CLASS(Decimal(4), 140),
                CLOCK_CLASS(Decimal(5), 6),
                CLOCK_CLASS(Decimal(6), 7),
                CLOCK_CLASS(Decimal(7), 150),
                CLOCK_CLASS(Decimal(8), 6),
                CLOCK_CLASS(Decimal(9), 7),
                CLOCK_CLASS(Decimal(10), 160),
            ),
            'result': True,
            'reason': None,
            'analysis': {
                "duration": 10,
                "clock_class_count": {
                    "FREERUN": {
                        "count": 1,
                        "transitions": {
                            "FREERUN": 1,
                            "LOCKED": 1,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "LOCKED": {
                        "count": 3,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 3,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_IN_SPEC": {
                        "count": 3,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 1,
                            "HOLDOVER_OUT_SPEC2": 1,
                            "HOLDOVER_OUT_SPEC3": 1
                        }
                    },
                    "HOLDOVER_OUT_SPEC1": {
                        "count": 1,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 1,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC2": {
                        "count": 1,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 1,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    },
                    "HOLDOVER_OUT_SPEC3": {
                        "count": 1,
                        "transitions": {
                            "FREERUN": 0,
                            "LOCKED": 0,
                            "HOLDOVER_IN_SPEC": 0,
                            "HOLDOVER_OUT_SPEC1": 0,
                            "HOLDOVER_OUT_SPEC2": 0,
                            "HOLDOVER_OUT_SPEC3": 0
                        }
                    }
                },
                "total_transitions": 9
            }
        },
    )
