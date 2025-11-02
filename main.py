from langgraph.graph import StateGraph, END
from agents.ingest_agent import ingest_data
from agents.clean_agent import clean_data
from agents.analyze_agent import analyze_data
from agents.report_agent import generate_report
from agents.features_agent import extract_features_and_insights
from agents.display_agent import display_report


# Define each node
def ingest_node(state):
    return ingest_data("datasets/earthquake_data_tsunami.csv")

def clean_node(state):
    return clean_data(state)

def analyze_node(state):
    return analyze_data(state)

def features_node(state):
    return extract_features_and_insights(state)

def report_node(state):
    return generate_report(state)

def display_node(state): 
    return display_report(state)

# Build LangGraph
builder = StateGraph(dict)

builder.add_node("ingest", ingest_node)
builder.add_node("clean", clean_node)
builder.add_node("analyze", analyze_node)
builder.add_node("features", features_node)
builder.add_node("report", report_node)
#builder.add_node("display", display_node)

# Define the execution flow
builder.set_entry_point("ingest")
builder.add_edge("ingest", "clean")
builder.add_edge("clean", "analyze")
builder.add_edge("analyze", "features")
builder.add_edge("features", "report")
#builder.add_edge("report", "display")

# Set final finish point
builder.set_finish_point("report")

# Compile and run
graph = builder.compile()

if __name__ == "__main__":
    output = graph.invoke({})
    print("✅ Report generated.")
    print(output["report"][:1000])  # print first 1000 chars of report
    print("📊 Dataset Shape:", output["df"].shape)
