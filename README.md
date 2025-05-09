
# Automated Code to Flowchart Generator

A Python-based tool that converts structured C++-like code into clean, interactive flowcharts.  
It combines lexical parsing, syntax tree generation, and flowchart rendering in real-time using PLY, Graphviz, and Streamlit.

---

## Features

- Real-time conversion of C++-like logic into flowcharts
- Lexer and Parser built using `ply.lex` and `ply.yacc`
- Visual representation using Graphviz (processes, decisions, loops)
- Syntax error feedback with user-friendly messages
- Streamlit-based frontend for instant interaction
- Modular code with clean separation: lexer, parser, renderer, frontend

---

## Project Structure

```

├── app.py               # Flask
├── main\_flowchart.py   # Graphviz flowchart generation logic
├── plytoken.py          # Token definitions (lexer)
├── plyparser.py         # Grammar rules (parser)
├── parsetab.py          # PLY-generated parser table
├── front.html           # Optional static UI (unused in Streamlit)
├── requirements.txt     # Required libraries

````

---

## 🛠️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/flowchart-generator.git
cd flowchart-generator
````

### 2. Create & Activate Virtual Environment

```bash
python -m venv env
.\env\Scripts\activate         # Windows
# source env/bin/activate      # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

---

## 📸 Sample Output

Input:

```cpp
int a = 5;
if (a > 2) {
    cout << "Big";
} else {
    cout << "Small";
}
```

Output:
Flowchart with:

* Start node
* Process block: `int a = 5`
* Decision node: `a > 2`
* Two branches: `cout << "Big"` and `cout << "Small"`
* End node

---

## Use Cases

* For students: Learn control flow visually
* For teachers: Demonstrate logic clearly
* For devs: Quickly document or debug logic
* For documentation: Auto-generate logic diagrams from code

---

## Future Scope

* Semantic validation (undeclared variables, unreachable code)
* Multi-language support (Python, Java, etc.)
* Better layout customization for large diagrams
* Integration with LMS or IDEs for grading and real-time visualization

---
