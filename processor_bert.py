from sentence_transformers import SentenceTransformer
import joblib

# Initialize Sentence Transformer model
transformer_model = SentenceTransformer('all-MiniLM-L6-v2')
# Load the classifier model
classifier_model = joblib.load("models/log_clf.joblib")


def classify_with_bert(log_message):

    # Generate embedding for the log message
    message_embedding = transformer_model.encode(log_message)

    probabilities = classifier_model.predict_proba([message_embedding])[0]


    if max(probabilities) < 0.5:
        return "Unclassified"
    predicted_class = classifier_model.predict([message_embedding])[0]


    return predicted_class # Return the classified label

if __name__ == "__main__":

    logs = [
        # "Server A790 was restarted unexpectedly during the process of data transfer",
        "hey bro chill babe"

    ]

    for log in logs:
        label = classify_with_bert(log)
        print(log,"->",label)
