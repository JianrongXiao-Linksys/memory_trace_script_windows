# Memory Trace Script (Windows)

Windows-based memory monitoring and analysis tool for Linksys routers.

## Overview

This tool collects system information from Linksys routers at regular intervals and generates Excel reports with memory usage trends. Useful for diagnosing memory leaks or tracking long-term memory behavior.

## How It Works

```
Router (sysinfo.cgi) → wget → Timestamped .txt files → Python Analysis → Excel Report
```

1. **Collection**: `get_sysinfo.py` fetches `/sysinfo.cgi` from router via HTTP
2. **Storage**: Saves as timestamped files (e.g., `192.168.1.1_sysinfo_2026-03-21_123456.txt`)
3. **Analysis**: Parses memory metrics from all collected files
4. **Report**: Generates Excel workbook with charts and statistics

## Scripts

### get_sysinfo.py

Continuous sysinfo collector running in background.

| Parameter | Default | Description |
|-----------|---------|-------------|
| `ip_lists` | `['192.168.1.1']` | Target router IP(s) |
| `default_username` | `admin` | HTTP auth username |
| `default_password` | `Linksys123!` | HTTP auth password |
| `wget_interval` | `3600` | Collection interval (seconds) |

### AI_Script_Memory_trace_from_sysinfo_Together.py

Analyzes collected sysinfo files and generates Excel report.

**Tracked Memory Metrics:**
- `MemAvailable` - Available memory (KB)
- `AnonPages` - Anonymous pages (KB)
- `SUnreclaim` - Slab unreclaimable (KB)

**Output Excel Sheets:**
- **DailyAverage**: Daily average values with bar charts
- **TimeSeries**: All data points with line charts

## Directory Structure

```
memory_trace_script_windows/
├── memory_trace_script_windows/
│   ├── get_sysinfo.py                              # Sysinfo collector
│   ├── AI_Script_Memory_trace_from_sysinfo_Together.py  # Analysis script
│   └── wget.exe                                    # Windows wget binary
└── README.md
```

## Usage

### Step 1: Collect Data

```bash
cd memory_trace_script_windows
python get_sysinfo.py
```

Let it run for hours/days to collect sufficient data points.

### Step 2: Analyze Data

```bash
# Run in the folder containing sysinfo .txt files
python AI_Script_Memory_trace_from_sysinfo_Together.py
```

### Output

Creates a timestamped folder containing:
- `Memory_Analysis_Combined_<folder_name>.xlsx` - Excel report with charts
- All original sysinfo `.txt` files (moved for archival)

## Requirements

- Python 3.x
- `openpyxl` library (`pip install openpyxl`)
- Windows OS (uses `wget.exe` and Windows subprocess flags)

## Configuration

Edit `get_sysinfo.py` to customize:

```python
ip_lists = ['192.168.1.1', '192.168.1.2']  # Multiple routers
default_username = 'admin'
default_password = 'your_password'
wget_interval = 1800  # 30 minutes
```

## Use Cases

- **Memory leak detection**: Track memory degradation over time
- **Firmware validation**: Compare memory behavior across firmware versions
- **Long-term stability testing**: Monitor memory during extended soak tests
