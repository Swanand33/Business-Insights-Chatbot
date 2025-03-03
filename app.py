from flask import Flask, request, jsonify, render_template
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

app = Flask(__name__)

# Load Advanced AI Model (Mistral-7B-Instruct)
print("⏳ Loading AI model... (This may take a few minutes)")
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

# Create chat pipeline
chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Invalid request. 'message' key is required."}), 400

    user_message = data['message']
    
    # Use structured prompting for better answers
    prompt = f"### Instruction: You are an AI assistant that provides business insights. Answer the following question professionally.\n\nUser: {user_message}\nAI:"
    
    response = chatbot(prompt, max_length=200, do_sample=True, temperature=0.7, top_k=50)
    
    # Extract AI response properly
    ai_reply = response[0]['generated_text'].split("AI:")[-1].strip()

    return jsonify({"response": ai_reply})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)