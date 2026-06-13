# InstruNet-Ai 🎵🤖

[![Live App](https://img.shields.io/badge/Live-Streamlit%20App-FF4B4B.svg)](https://instrument-ai.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![Deep Learning](https://img.shields.io/badge/Deep%20Learning-TensorFlow%20%2F%20Keras-orange.svg)](https://tensorflow.org/)

InstruNet-Ai is an advanced, end-to-end Machine Learning web application designed to classify and detect musical instruments from raw audio input. Powered by a deep convolutional neural network (CNN) backend and wrapped in an intuitive Streamlit interface, the platform converts temporal audio signals into localized visual features to predict musical instrumentation with high precision.

## 🚀 Live Demo
**Test the live AI model here:** [InstruNet-Ai Web Deployment](https://instrument-ai.streamlit.app/)

## ✨ Key Engineering Features
* **Advanced Audio Pipeline:** Seamlessly handles user-uploaded audio files (`.mp3`, `.wav`) and processes them dynamically into standardized data segments.
* **Time-Frequency Feature Extraction:** Utilizes Short-Time Fourier Transforms (STFT) to compute Mel-scaled spectrograms, converting 1D waveforms into 2D structural image features that capture acoustic timbres.
* **Deep CNN Architecture:** Leverages an optimized Deep Learning classifier trained to identify complex acoustic patterns across multiple instrument classes.
* **Instantaneous Cloud Inference:** Lightweight, high-speed deployment structure optimized for near-zero latency execution on Streamlit Community Cloud.

## 🛠️ Technical Architecture & Stack
* **Frontend/UI:** Streamlit (Python-native reactive framework)
* **Core ML & Deep Learning:** TensorFlow, Keras
* **Audio Signal Processing:** Librosa, SoundFile, NumPy
* **Data Visualization:** Matplotlib (for real-time Mel-spectrogram rendering)
* **Version Control & Hosting:** GitHub, Streamlit Cloud

## 🧠 Architectural Challenges & Solutions

**1. Transforming Temporal Audio Signals into Trainable Features**
* **Challenge:** Raw 1D audio amplitudes vary dramatically in duration, amplitude, and sampling rates, making them highly inefficient for standard deep neural networks to process directly.
* **Solution:** Engineered a robust preprocessing pipeline using `librosa` to resample and segment audio inputs. By applying Log-Mel Spectrogram extraction, the temporal signals were mapped into 2D time-frequency representations, allowing the model to leverage mathematical spatial relationships much like a computer vision model processes images.

**2. Optimizing Heavy ML Model Latency for Serverless Cloud Deployment**
* **Challenge:** Deep learning libraries (like TensorFlow) and heavy model weight objects can consume substantial memory, resulting in sluggish processing speeds or container crashes within resource-constrained serverless cloud environments.
* **Solution:** Structured the deployment codebase efficiently by separating training pipelines from active production inference. Implemented aggressive runtime caching routines (`@st.cache_resource`) to load the underlying neural network into memory exactly once, preventing memory overhead spikes during subsequent client predictions.

## 💻 Local Installation & Reproducibility

Follow these steps to configure and run InstruNet-Ai on your local workstation:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Subhajitindia99das/InstruNet-Ai.git](https://github.com/Subhajitindia99das/InstruNet-Ai.git)
   cd InstruNet-Ai

2. **Set up a clean virtual environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt

4. **Launch the web interface:**
   ```bash
   streamlit run app.py


The application will automatically spin up on your local network at http://localhost:8501

Designed and Engineered by Subhajit Das
