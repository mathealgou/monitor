<h1 style="text-align: center;">Monitor 🖥️</h1>

<h2 style="text-align: center;">
Something to leave on the second monitor while you game on the first.
</h2>

![Monitor](./doc/Screenshot.png)

### Installation

#### Windows

In the `/dist` directory of this repository, you will find a `main.exe` file. This is the executable for the Monitor application. You can run this file directly without any additional installation.

### Build from source

##### Build from source

1. Requirements

To build the Monitor application from source, you will need the following:

- [Python 3.12](https://www.python.org/downloads/)

- [Pip](https://pip.pypa.io/en/stable/installation/)

2. Clone the repository

```bash
git clone https://github.com/mathealgou/monitor.git
```

3. Install the dependencies

```bash
python -m venv .venv
```

```powershell
# Windows
.\.venv\Scripts\Activate
```

```bash
# Linux/Mac
source .venv/bin/activate
```

4. Run the build script

```bash
pyinstaller --onefile --noconsole main.py
```
