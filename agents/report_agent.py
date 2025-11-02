from llama_cpp import Llama
import os
import json

# Initialize the local LLM
llm = Llama(
    model_path="models/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    n_ctx=8192,
    n_gpu_layers=-1,
    use_gpu=True,
    verbose=False
)

# Helper function to summarize a section (e.g., summary stats, correlation)
def summarize_section(section_name, section_data):
    if not section_data:
        return ""

    prompt = f"""
You are a helpful data assistant.

Summarize the following {section_name} into clear and concise plain English insights. Use bullet points. Avoid raw tables or exact numbers.

### {section_name.upper()} DATA:
{json.dumps(section_data, indent=2)}

Write a professional summary:
"""

    try:
        result = llm(prompt, max_tokens=512, stop=["</s>"])
        return result['choices'][0]['text'].strip()
    except Exception as e:
        return f"(Failed to summarize {section_name}: {str(e)})"

# Main LangGraph-compatible report node
def generate_report(state: dict) -> dict:
    eda = state.get("eda", {})
    if not eda:
        raise ValueError("No EDA data found in state for reporting.")

    # Section-wise LLM summarization
    sections = {
        "Summary statistics": eda.get("summary", {}),
        "Correlation matrix": eda.get("correlation", {}),
        "Value counts": eda.get("value_counts", {}),
    }

    full_report = ""
    for section_name, section_data in sections.items():
        summary = summarize_section(section_name, section_data)
        if summary:
            full_report += f"## {section_name}\n\n{summary}\n\n"

    # Save to disk
    os.makedirs("outputs", exist_ok=True)

    with open("outputs/report.txt", "w", encoding="utf-8") as f:
        f.write(full_report)

    with open("outputs/report.md", "w", encoding="utf-8") as f:
        f.write("# 🧠 Data Analysis Report\n\n")
        f.write(full_report.replace("\n", "\n\n"))  # Add spacing

    return {
        **state,
        "report": full_report,
        "report_path": "outputs/report.txt",
        "report_status": "report_generated"
    }
