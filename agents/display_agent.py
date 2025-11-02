import gradio as gr
import os

def display_report(state: dict) -> dict:
    report = state.get("report", "No report found.")
    report_path = state.get("report_path", "outputs/report.txt")

    def show_report():
        return report

    with gr.Blocks(title=" Data Analysis Report Viewer") as demo:
        gr.Markdown("# AI-Generated EDA Report")
        gr.Markdown("Below is your AI-generated report from your dataset.")
        gr.Textbox(show_report, lines=30, label="Report", interactive=False)
        gr.File(label="Download Report", value=report_path, interactive=False)
        gr.Button("Close").click(fn=demo.close, inputs=[], outputs=[])

    demo.launch(share=False)

    return {
        **state,
        "status": "displayed"
    }
