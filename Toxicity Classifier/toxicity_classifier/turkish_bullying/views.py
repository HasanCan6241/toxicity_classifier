# turkish_bullying/views.py
from django.shortcuts import render
from transformers import AutoTokenizer, TFBertForSequenceClassification, TextClassificationPipeline

# Model ve tokenizer'ı yükleyin
tokenizer = AutoTokenizer.from_pretrained("nanelimon/bert-base-turkish-bullying")
model = TFBertForSequenceClassification.from_pretrained("nanelimon/bert-base-turkish-bullying", from_pt=True)

# Pipeline oluşturun
pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer, return_all_scores=True, top_k=4)

def index(request):
    if request.method == "POST":
        text = request.POST.get("text")
        result = pipe(text)

        formatted_result = [
            {"label": item["label"], "score": item["score"]}
            for item in result[0]
        ]

        return render(request, "index.html", {"result": formatted_result, "text": text})
    return render(request, "index.html")

def model(request):
    if request.method == "POST":
        text = request.POST.get("text")
        result = pipe(text)

        formatted_result = [
            {"label": item["label"], "score": item["score"]}
            for item in result[0]
        ]

        return render(request, "model.html", {"result": formatted_result, "text": text})
    return render(request,"model.html")