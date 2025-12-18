# Library-Management-System

## 🚀 Development Setup

### 1. Clone the repository

```bash
git clone https://github.com/MarwanULQ/Library-Management-System.git
cd Library-Management-System

```

### 2. Create and activate a virtual environment
## For linux/macOS

```bash
python -m venv venv
source .venv/bin/activate

```
## For Windows
```
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### if new dependencies are added
```bash
pip freeze > requirements.txt
```

### 4. Running the frontend

```bash
streamlit run src/library_management/ui/app.py
```
