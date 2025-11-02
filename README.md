#  LangGraph EDA Copilot – Local, Multi-Agent Data Science Assistant

An intelligent, agent-based Exploratory Data Analysis (EDA) pipeline built with **LangGraph**, powered by **open-source LLMs** like **Mistral-7B**, and served via **Gradio UI**.

Upload any CSV dataset → Let the pipeline ingest, clean, analyze, summarize, and generate a human-readable report, right in your browser, all running **locally** on your GPU 

---

## 🚀 Demo Preview

![](https://github.com/prakhar105/langgraph-eda-copilot/blob/master/assests/img.png)

---

##  Architecture

```
            ┌────────────┐
            │ CSV Upload │ ◀── via Gradio
            └────┬───────┘
                 ▼
          ┌─────────────┐
          │  Ingest     │ ← pandas
          └────┬────────┘
               ▼
          ┌─────────────┐
          │  Clean      │ ← nulls, types, fill
          └────┬────────┘
               ▼
          ┌─────────────┐
          │  Analyze    │ ← stats, correlation
          └────┬────────┘
               ▼
          ┌─────────────┐
          │  Features   │ ← high-card cols, skew, etc.
          └────┬────────┘
               ▼
          ┌─────────────┐
          │  Report     │ ← Mistral LLM (llama-cpp)
          └────┬────────┘
               ▼
          ┌──────────────┐
          │  Gradio UI   │ ← Report shown & downloadable
          └──────────────┘
```

---

##  Tech Stack

| Component     | Description                              |
|---------------|------------------------------------------|
| LangGraph     | Multi-agent orchestration framework      |
| pandas        | Data ingestion, cleaning, transformation |
| llama-cpp     | Local inference of Mistral-7B LLM        |
| Gradio        | Simple UI for file upload & report view  |
| matplotlib    | *(Optional)* for charting                |
| Python 3.10+  | Compatible with `llama-cpp`              |

---

##  Setup Instructions

### 1. Clone this Repo

```bash
git clone https://github.com/yourusername/langgraph-eda-copilot.git
cd langgraph-eda-copilot
```

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

pip install -r requirements.txt
```

### 3. Download Model (One-Time)

Download [Mistral-7B-Instruct Q4_K_M](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF) and place it in:

```
models/mistral-7b-instruct-v0.1.Q4_K_M.gguf
```

### 4. Run the Gradio App

```bash
python gradio_app.py
```

 Upload a CSV → Report gets generated and displayed in your browser.

---

##  Features

-  Agent-based modular design using LangGraph
-  Automatic data cleaning (nulls, types, imputation)
-  Descriptive stats, correlation matrix, skewness
-  Feature insights (high-cardinality, missing %, etc.)
-  LLM-generated report using locally-run Mistral-7B
-  Gradio UI: file upload + view + download

---

##  Project Structure

```
langgraph-eda-copilot/
├── agents/
│   ├── ingest_agent.py
│   ├── clean_agent.py
│   ├── analyze_agent.py
│   ├── features_agent.py
│   ├── report_agent.py
│   └── display_agent.py (optional)
├── datasets/
│   └── sample.csv
├── outputs/
│   └── report.txt / report.md
├── models/
│   └── mistral-7b-instruct-v0.1.Q4_K_M.gguf
├── main.py
├── gradio_app.py
└── README.md
```

---

##  Future Additions

-  Matplotlib/Plotly charts in Gradio
-  Export report as PDF
-  Chat with your dataset
-  HuggingFace Space / Docker release

---

##  Credits

- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Mistral LLM](https://huggingface.co/mistralai)
- [TheBloke Quantized GGUFs](https://huggingface.co/TheBloke)
- [Gradio](https://gradio.app)

---

##  License

MIT License - use freely, improve openly, and attribute kindly.