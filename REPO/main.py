import csv
import replicate

# Create an empty list to store data for each iteration
data_list = []

for i in range(1930, 2031, 10):
    location = "C:/Users/Dell/Desktop/STARC/Frames/frame" + str(i) + ".jpg"
    output = replicate.run(
        "nelsonjchen/minigpt-4_vicuna-13b:c1f0352f9da298ac874159e350d6d78139e3805b7e55f5df7c5b79a66ae19528",
        input={"image": open(location, "rb"), "message": "Detect which shot is played by the batman?"}
    )

    # Assuming 'output' is a list containing the predictions for each iteration
    # Join the list elements to create a single sentence
    prediction_sentence = " ".join(output)

    # Append the current value of i and the prediction_sentence to the data_list
    data_list.append([i, prediction_sentence])

# Open the file in write mode
output_file_path = "prediction.csv"
with open(output_file_path, 'w', newline='') as csv_file:
    # Create a CSV writer object
    writer = csv.writer(csv_file)

    # Write the data to the file with headers for each column
    writer.writerow(["Iteration", "Prediction"])
    writer.writerows(data_list)
