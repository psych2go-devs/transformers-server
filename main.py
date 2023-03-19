from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
from pydantic import BaseModel
from fastapi import FastAPI
import tensorflow as tf
import os

MODEL_PATH = os.environ.get("MODEL_PATH", "./cookie")

id2label = {0: "IGNORE", 1: "REACT"}
label2id = {"IGNORE": 0, "REACT": 1}

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-cased")
model = TFAutoModelForSequenceClassification.from_pretrained(
    MODEL_PATH, num_labels=2, id2label=id2label, label2id=label2id
)


def classify(text: str):
    return tf.math.argmax(
        model(**tokenizer(text, return_tensors="tf")).logits, axis=-1
    )[0]


app = FastAPI()


class Inference(BaseModel):
    text: str


@app.post("/cookie")
def cookie(inference: Inference):
    classification = int(classify(inference.text))
    return {"id": classification, "label": model.config.id2label[classification]}
