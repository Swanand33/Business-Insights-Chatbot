# 🚀 AI Chatbot for Business Insights (Hugging Face-Only)

This is a **fully customizable AI chatbot** that runs on **Hugging Face models** without requiring OpenAI. Users can **integrate their own Hugging Face models and API keys**, making this a **flexible, mold/template** chatbot that can be adapted for different business needs.

---

## ✨ **Features**
✅ **No OpenAI Dependency** – Uses only Hugging Face models 📌  
✅ **Customizable AI Models** – Choose any model from Hugging Face 🤖  
✅ **Local or Cloud Support** – Run models **locally** or via API ☁️  
✅ **Modern Chat Interface** – Responsive UI (2025-ready) 🎨  
✅ **Built with Flask & Transformers** – Optimized for performance ⚡  

---

## 🏗 **How to Use**

### **1️⃣ Install Dependencies**  
Run the following command in your project folder:
```bash
pip install -r requirements.txt
```

### **2️⃣ Set Up Hugging Face API Key & Model**  
Create a `.env` file in the project root and add:
```ini
# Hugging Face API Token (Needed for hosted models)
HUGGINGFACE_TOKEN=your-huggingface-token

# Choose the Hugging Face model (Change if needed)
MODEL_NAME=microsoft/DialoGPT-medium
```
👉 **Replace `your-huggingface-token` with your own Hugging Face API key.**  
👉 **Change `MODEL_NAME` to any model from [Hugging Face Models](https://huggingface.co/models).**  

### **3️⃣ Run the Flask Server**
```bash
python app.py
```

### **4️⃣ Open Chatbot in Browser**
Visit:
```
http://127.0.0.1:5000/
```
Type a message and start chatting with your AI model! 🎉

---

## ⚙ **How It Works**
This chatbot is designed as a **mold/template** where users can:
- **Integrate any Hugging Face model** by updating the `.env` file.
- **Run models locally** (downloaded) or **via API** (cloud-based models).
- **Modify and enhance the UI** to match business needs.

---

## 📂 **Project Structure**
```
Chatbot-for-business/
├── app.py                # Backend (Flask API)
├── requirements.txt      # Dependencies
├── .env                  # Environment Variables
│
├── templates/            # Frontend UI
│   ├── index.html        # Main chat page
│
├── static/               # Static Files (CSS & JS)
│   ├── css/style.css     # Chatbot UI styling
│   ├── js/script.js      # Handles chat interactions
│
└── README.md             # Project Documentation
```

---

## 🎨 **Screenshots**


---

## 🌎 **Customizing Your AI Model**
To change the AI model:
1. **Find a model** on [Hugging Face](https://huggingface.co/models).
2. **Update the `.env` file** with the new model name.
3. **Restart the Flask server** (`python app.py`).

---

## 🚀 **Deployment (Optional)**
To deploy this chatbot on a server:
1. Use **Render, Heroku, or Streamlit** for hosting.
2. Install Gunicorn for production servers:
   ```bash
   pip install gunicorn
   ```
3. Deploy using cloud services with Hugging Face models.

---

## 🤝 **Contributing**
This is an open-source project! Feel free to fork, modify, and improve it. 🚀

---

