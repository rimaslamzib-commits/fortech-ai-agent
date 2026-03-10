from predictor import predict_match

print("⚽ FORTECH V2.1 BOOST AI ENGINE")

stats = input("Paste Forebet match statistics: ")

prediction = predict_match(stats)

print("AI Prediction:", prediction)
