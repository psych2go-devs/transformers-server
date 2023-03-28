from transformers import AutoTokenizer, AutoModelForSequenceClassification
from pydantic import BaseModel
from fastapi import FastAPI
import torch
import os

COOKIE_MODEL_PATH = os.environ.get("MODEL_PATH", "./cookie")

id2label = {0: "NO", 1: "YES"}
label2id = {"NO": 0, "YES": 1}

cookie_tokenizer = AutoTokenizer.from_pretrained("distilbert-base-cased")
cookie_model = AutoModelForSequenceClassification.from_pretrained(
    COOKIE_MODEL_PATH, num_labels=2, id2label=id2label, label2id=label2id
)


def analyze_cookie_message(text: str):
    while torch.no_grad():
        return (
            cookie_model(**cookie_tokenizer(text, return_tensors="pt"))
            .logits.argmax()
            .item()
        )


app = FastAPI()


class Inference(BaseModel):
    text: str


@app.post("/cookie")
def cookie(inference: Inference):
    analysis = analyze_cookie_message(inference.text)
    return {"id": analysis, "label": cookie_model.config.id2label[analysis]}
