#!/bin/bash
echo "==================================="
echo "  Telegram Channels Manager"
echo "==================================="
echo "1. Download Channels (导出频道)"
echo "2. Load Channels (导入频道)"
echo "==================================="
read -p "Please select an option (1 or 2): " choice

USE_PROXY=$(python -c "import json; print(str(json.load(open('proxy_config.json'))['use_proxy']).lower())")
PROXY_URL=$(python -c "import json; print(json.load(open('proxy_config.json'))['proxy_url'])")

if [ "$USE_PROXY" = "true" ]; then
    echo "[Info] Using proxy: $PROXY_URL"
    export HTTP_PROXY=$PROXY_URL
    export HTTPS_PROXY=$PROXY_URL
    export ALL_PROXY=$PROXY_URL
else
    echo "[Info] Proxy is disabled in config."
    unset HTTP_PROXY
    unset HTTPS_PROXY
    unset ALL_PROXY
fi

if [ -f ".venv/Scripts/python" ]; then
    PYTHON_CMD=".venv/Scripts/python"
elif [ -f ".venv/bin/python" ]; then
    PYTHON_CMD=".venv/bin/python"
else
    PYTHON_CMD="python"
fi

if [ "$choice" = "1" ]; then
    $PYTHON_CMD Download_Channels.py
elif [ "$choice" = "2" ]; then
    $PYTHON_CMD Load_Channels.py
else
    echo "Invalid choice!"
fi
