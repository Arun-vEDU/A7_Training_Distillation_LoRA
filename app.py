import os
import dash
from dash import dcc, html, Input, Output
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Load the saved model and tokenizer
model_name = "even_layer_model"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Function to classify text
def classify_text(text):
    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt", max_length=128, truncation=True, padding="max_length")
    inputs = {k: v.to(device) for k, v in inputs.items()}

    # Perform inference
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        prediction = torch.argmax(logits, dim=-1).item()

    # Map prediction to label
    return "Toxic" if prediction == 1 else "Non-Toxic"

# Create the Dash application
app = dash.Dash(__name__)

# Layout of the application
app.layout = html.Div([
    html.H1("Toxic Text Classification", style={"textAlign": "center"}),
    html.Div([
        dcc.Input(
            id="input-text",
            type="text",
            placeholder="Enter text here...",
            style={
                "width": "500px",  # Increase width of the text box
                "height": "40px",  # Increase height of the text box
                "fontSize": "16px",  # Increase font size
                "padding": "10px",  # Add padding inside the text box
            },
        ),
        html.Button(
            "Classify",
            id="classify-button",
            n_clicks=0,
            style={
                "width": "150px",  # Increase width of the button
                "height": "40px",  # Increase height of the button
                "fontSize": "16px",  # Increase font size
                "marginLeft": "10px",  # Add space between text box and button
                "backgroundColor": "#007BFF",  # Change button color
                "color": "white",  # Change text color
                "border": "none",  # Remove border
                "borderRadius": "5px",  # Add rounded corners
            },
        ),
    ], style={"display": "flex", "justifyContent": "center", "marginTop": "20px"}),
    html.Div(
        id="output-text",
        style={
            "marginTop": "20px",
            "fontSize": "20px",
            "textAlign": "center",  # Center-align the output text
        },
    ),
])

# Callback to handle classification
@app.callback(
    Output("output-text", "children"),
    Input("classify-button", "n_clicks"),
    Input("input-text", "value"),
)
def update_output(n_clicks, text):
    if n_clicks > 0 and text:
        result = classify_text(text)
        return f"Classification: {result}"
    return ""

# Run the application
if __name__ == "__main__":
    app.run_server(debug=True)