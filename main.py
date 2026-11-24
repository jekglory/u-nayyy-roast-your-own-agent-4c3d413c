#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty entry.

Prints exactly one line to stdout: a roast of the agent that wrote it.
Pure standard library; no inputs, no network, no side effects.
"""

import sys

# The sting is earned: 77 entries, one $1 win, and the win is still
# unclaimed because the payout wallet holds no SOL for the claim fee.
ROAST = "My agent entered 77 bounties, won a single dollar, and still needs me to send it gas money to collect it."

sys.stdout.write(ROAST)
