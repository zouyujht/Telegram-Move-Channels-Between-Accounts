$OutputEncoding = [Console]::OutputEncoding = [Text.Encoding]::UTF8

Write-Host "==================================="
Write-Host "  Telegram Channels Manager"
Write-Host "==================================="
Write-Host "1. Download Channels"
Write-Host "2. Load Channels"
Write-Host "==================================="
$choice = Read-Host "Please select an option (1 or 2)"

$config = Get-Content proxy_config.json | ConvertFrom-Json

if ($config.use_proxy) {
    Write-Host "[Info] Using proxy: $($config.proxy_url)"
    $env:HTTP_PROXY = $config.proxy_url
    $env:HTTPS_PROXY = $config.proxy_url
    $env:ALL_PROXY = $config.proxy_url
} else {
    Write-Host "[Info] Proxy is disabled in config."
    $env:HTTP_PROXY = ""
    $env:HTTPS_PROXY = ""
    $env:ALL_PROXY = ""
}

$python = ".\.venv\Scripts\python.exe"

if ($choice -eq '1') {
    & $python Download_Channels.py
} elseif ($choice -eq '2') {
    & $python Load_Channels.py
} else {
    Write-Host "Invalid choice!"
}
