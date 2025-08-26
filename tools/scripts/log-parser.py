#!/usr/bin/env python3
"""
Simple log parser for SOC practice
"""

import re

def parse_log_line(line):
    pattern = r'(?P<timestamp>\S+) (?P<host>\S+) (?P<user>\S+) (?P<action>.+)'
    match = re.match(pattern, line)
    if match:
        return match.groupdict()
    return None

if __name__ == "__main__":
    with open("sample.log") as f:
        for line in f:
            parsed = parse_log_line(line)
            if parsed:
                print(parsed)
