from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)  # Create API

# Load dataset
file_path =r"C:\Users\sidpa\OneDrive\Dokumenty\python\Python api dataset.csv"
  # Ensure correct path
df = pd.read_csv(r"C:\Users\sidpa\OneDrive\Dokumenty\python\Python api dataset.csv")  # Read CSV file
data_dict = df.to_dict(orient="records")  # Convert data to dictionary format

# Homepage message
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Rainfall API!"})

# Get all data
@app.route("/data", methods=["GET"])
def get_all_data():
    return jsonify(data_dict)

if __name__ == "__main__":
    app.run(debug=True)  # Start API
