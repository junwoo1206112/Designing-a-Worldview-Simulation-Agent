#!/bin/bash
# 라프라시아 야구 시뮬레이션 RPG - Diamond & Magic

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Create directories if they don't exist
mkdir -p saves logs

echo ""
echo "╔════════════════════════════════════════════════════════╗"
echo "║   라프라시아 야구 시뮬레이션 RPG                       ║"
echo "║   \"Diamond & Magic\"                                    ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""

python3 engine.py
