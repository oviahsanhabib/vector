# Rickroll on Vectorx 

This guide provides step-by-step instructions on setting up Vectorx server using the [Vectorx Python SDK](https://github.com/fforchino/vectorx).

## Prerequisites

Before you begin, make sure you have the following prerequisites:

- [Vectorx Server](https://github.com/fforchino/vectorx)
- SSH client (e.g., MobaXterm or PuTTY)

## Setup Instructions

### Step 1: SSH to Vectorx Server

Connect to the Vectorx server using your preferred SSH client.

### Step 2: Initial Configuration
Navigate to the vector-python-sdk directory and run the configuration script.

cd /home/pi/vector-python-sdk/wirepod/
cp -r /path/to/assets .
cp /path/to/rickroll.py .

```bash
cd /home/pi/vector-python-sdk/
```
```bash
python3 configure.py
```
### Step 3: Copy Assets and Script
Move to the wirepod directory and copy the assets folder and rickroll.py file.

```bash
cd /home/pi/vector-python-sdk/wirepod/
```
### Step 4: Run the Script
Execute the rickroll.py script.

```bash
./rickroll.py
```
### Step 5: Add Custom Intent
Follow the provided screenshot to add a custom intent for voice commands.
