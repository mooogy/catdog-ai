from torchvision.models import resnet50, ResNet50_Weights
import torch
from PIL import Image

def getEmbeddingPipeline():
    preprocess = ResNet50_Weights.DEFAULT.transforms()
    resnet = resnet50(weights=ResNet50_Weights.DEFAULT)
    resnet.eval()
    feature_extractor = torch.nn.Sequential(*list(resnet.children())[:-1])
    return preprocess, feature_extractor

def getEmbedding(img: Image.Image, preprocess, feature_extractor):
    input_tensor = preprocess(img).unsqueeze(0)
    with torch.no_grad():
        embedding = feature_extractor(input_tensor)
        embedding = embedding.view(1, -1)

    return embedding.numpy()