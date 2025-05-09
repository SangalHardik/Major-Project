## Automated Code to Flowchart Generator
Convert structured C++-like source code into dynamic flowcharts using AI-powered parsing and visualization.

---

## Features

- Real-time flowchart generation via browser
- Lexical and syntax analysis using PLY (`lex`, `yacc`)
- Graphviz-powered flowchart rendering
- Syntax error detection and messaging
- Supports: `if`, `else`, `for`, `while`, `cin`, `cout`
- Works with nested blocks, I/O, and conditions

---

## Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/your-username/flowchart-generator.git
cd flowchart-generator

# 2. Create a virtual environment
python -m venv env
.\env\Scripts\activate  # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the app
streamlit run app.py
````

---

## Project Structure

```bash
├── app.py               # Streamlit frontend
├── views.py             # Core backend orchestration
├── pdf_ingest.py        # Optional: PDF parsing agent
├── sql_agent.py         # Optional: SQL query agent
├── plyparser.py         # Grammar + parser (PLY)
├── plytoken.py          # Tokenizer (PLY lexer)
├── requirements.txt     # Python dependencies
├── sample.pdf           # Sample input
```

---

## 🧪 Sample Output

> Sample C++-like input:

```cpp
int a = 5;
if (a > 2) {
    cout << "Big";
} else {
    cout << "Small";
}
```

> Resulting Flowchart:
> ![Flowchart Screenshot](images/sample-flowchart.png)

---

## Use Cases

* Beginners learning programming logic
* Visual aid for teaching control flow
* Flowchart creation for documentation
* Debugging complex logic structures

---

## Future Improvements

* Semantic analysis and deeper code checks
* Multi-language support (Python, Java)
* Drag-and-drop visual editing
* LMS/IDE integration for grading

---
