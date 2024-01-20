# Rickroll on Vectorx 
![Screenshot 2024-01-19 221955](https://github.com/oviahsanhabib/vector/assets/104899177/47c46ef9-7969-4a2b-b46e-d601d7c7644a)

This guide provides step-by-step instructions on setting up Vectorx server using the [Vectorx Python SDK](https://github.com/fforchino/vectorx).

## Prerequisites

Before you begin, make sure you have the following prerequisites:

- [Vectorx Server](https://github.com/fforchino/vectorx)
- SSH client (e.g., MobaXterm or PuTTY)

## Setup Instructions

### Step 1: SSH to Vectorx Server

Connect to the Vectorx server using your preferred SSH client.
![Screenshot 2024-01-19 221539](https://github.com/oviahsanhabib/vector/assets/104899177/d2a5265d-e05c-467f-b8bf-f6e013b38b93)

### Step 2: Initial Configuration
Navigate to the vector-python-sdk directory and run the configuration script.

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
![Screenshot 2024-01-19 221825](https://github.com/oviahsanhabib/vector/assets/104899177/520e219e-29e0-4846-a77a-a3961a3ea3dc)
