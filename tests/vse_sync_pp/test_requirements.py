### SPDX-License-Identifier: GPL-2.0-or-later

"""Test cases for vse_sync_pp.requirements"""

### ensure values in REQUIREMENTS have to be changed in two places

from unittest import TestCase

from vse_sync_pp.requirements import REQUIREMENTS


class TestRequirements(TestCase):
    """Test cases for vse_sync_pp.requirements.REQUIREMENTS"""
    def test_g8272_prtc_a(self):
        """Test G.8272/PRTC-A requirement values"""
        self.assertEqual(
            REQUIREMENTS['G.8272/PRTC-A'],
            {
                'time-error-in-locked-mode/ns': 100,
            },
        )

    def test_g8272_prtc_b(self):
        """Test G.8272/PRTC-B requirement values"""
        self.assertEqual(
            REQUIREMENTS['G.8272/PRTC-B'],
            {
                'time-error-in-locked-mode/ns': 40,
            },
        )
