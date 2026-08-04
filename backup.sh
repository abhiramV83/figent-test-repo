#!/bin/bash
# DELIBERATE SECURITY ISSUE: command injection
echo "Starting backup for path: $1"
eval "tar -czf backup.tar.gz $1"
