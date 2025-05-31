# CatDog AI Classifier App

**How cat-like is your dog? How dog-like is your cat?**

**Upload an image to instantly find out whether it's more cat or more dog with visualized decision boundaries and model confidence scores.**


## Table of Contents
- [Screenshots](#screenshots)
- [Description](#description)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Tech Stack / Libraries Used](#tech-stack--libraries-used)
- [License](#license)

---

##  Screenshots

>  Landing Section:
![Landing Section where the user can upload an image to be classified](assets/landing.png)

>  Results After The User Uploads An Image:
![Results section which displays the predicted class of the image, the logistic regression probabilities of each label, and a graph showing the decision boundary](assets/results.png)

---

##  Description

This project is a full-stack image classifier web app that:
- Lets users upload images of cats and dogs
- Uses pretrained ResNet50 embeddings with KNN and Logistic Regression classifiers
- Shows prediction results + a 2D visual of the model's decision space

All models and EDA are built in this **repo**:
[Cat vs Dog Image Analysis – EDA & Model Selection](https://github.com/mooogy/catdog-image-analysis)

---

## Installation

### Option 1: Using Docker (**Recommended**)

**Requires Docker to be installed on your machine**

```bash
docker pull mooogy/catdog-ai
docker run -p 8000:8000 mooogy/catdog-ai # launches at http://localhost:8000
```

### Option 2: Local Setup using Python + Make

**With Make**

```bash
git clone https://github.com/mooogy/catdog-ai.git
cd catdog-ai
make run  # launches at http://localhost:8000
```

### **OR**

**Without Make**
```bash
git clone https://github.com/mooogy/catdog-ai.git
cd catdog-ai
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload  # launches at http://localhost:8000
```

---

## How to Use

1. Open your browser and go to [http://localhost:8000](http://localhost:8000)
2. Upload an image of a cat or dog
3. View the prediction, model probabilities, and decision boundary
4. Use the reset button to try a new image

---

## Tech Stack / Libraries Used

### Technologies
- **HTML, CSS, Javascript** - Frontend UI/UX, responsive layout, file upload preview
- **Python** – Backend and machine learning
- **Docker** – Cross-platform deployment
- **Makefile** - Easy virtual environment setup and development

### Libraries
- **Torch** (Torch, TorchVision) - Used for loading the pretrained ResNet model and extracting image embeddings
- **Scikit-learn** - Handles PCA dimensionality reduction, classification models (KNN, Logistic Regression)
- **FastAPI** – Backend API for handling image uploads and returning model predictions
- **Pillow** - Processes and resizes uploaded images
- **Plotly** - Generates decision boundary graph for the frontend

---

## License

This project is licensed under the [MIT License](LICENSE).
