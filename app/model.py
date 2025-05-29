import joblib
from app.embedding import getEmbedding, getEmbeddingPipeline
from app.plot import plotly_decision_boundary
import plotly.graph_objects as go
import numpy as np
from PIL import Image

# Load model once on import
knn_classifier = joblib.load("model/knn_classifier_1000d.pkl")
knn_visualizer = joblib.load("model/knn_visualizer_bundle.pkl")
logreg_model =joblib.load("model/logreg_classifier.pkl")
preprocess, feature_extractor = getEmbeddingPipeline()

def label_from_image(image: Image.Image):
    embedding = getEmbedding(image, preprocess, feature_extractor)
    label = knn_classifier.predict(embedding)[0]
    labels = ["Cat", "Dog"]

    return labels[label]


def probs_from_image(image: Image.Image):
    embedding = getEmbedding(image, preprocess, feature_extractor)  # shape: (1, 2048)
    probs = logreg_model.predict_proba(embedding)[0]  # Get probability vector
    labels = ["cat", "dog"]

    return {label: float(prob) for label, prob in zip(labels, probs)}



def plot_from_image(image: Image.Image):
    # Load model bundle
    model = knn_visualizer["model"]
    X_2d = knn_visualizer["X_2d"]
    y = knn_visualizer["y"]

    # Get 2048D embedding, then 2D projection and prediction
    embedding = getEmbedding(image, preprocess, feature_extractor)
    point_2d = model.named_steps["pca"].transform(embedding)[0]
    pred_label = model.predict(embedding)[0]

    fig = plotly_decision_boundary(X_2d, y, point_2d, pred_label, model.named_steps['knn'])

    return fig