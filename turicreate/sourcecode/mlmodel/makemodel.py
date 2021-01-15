import turicreate as tc
import os

dataSetDirPath = os.path.join(os.getcwd(),'dataset/')

print('Loading images from ', dataSetDirPath)
sfData = tc.image_analysis.load_images(dataSetDirPath, with_path=True, recursive=True, ignore_failure=True)

print("Number of Colums : ", sfData.num_columns(), "\nNumber of Rows : ", sfData.num_rows())

sfData['label'] = sfData["path"].apply(lambda path: os.path.basename(os.path.dirname(path)))

print("Number of Colums : ", sfData.num_columns(), "\nNumber of Rows : ", sfData.num_rows())
print('Unique labels ', sfData['label'].unique())

training_data, test_data = sfData.random_split(0.8) # 80% training data
model = tc.image_classifier.create(training_data, target="label")

predict = model.predict(test_data)
metrics = model.evaluate(test_data)

# metrics.explore()

print("Accuracy of model", metrics["accuracy"])

print("Saving model..")
model.save("turidogcatv2.model")


print('Completed, Saved mode with name turidogcatmdl.model')


