# Food Recognition 

This project focuses on developing a machine learning model for recognizing various types of foods using DenseNet and MobileNet architectures. The project includes training, testing, and fine-tuning deep learning models, along with evaluating their performance using various metrics.

## Project Structure

- **models/**
  - Contains trained model checkpoints and logs for different model architectures and configurations.
  - `densenet121`, `densenet121-1b`, `densenet161-1b-sch`, etc.: Model checkpoint files.
  - **logs/**: Logs generated during model training, useful for debugging and performance monitoring.

- **notebooks/**
  - Jupyter notebooks for training, testing, and plotting.
  - `training.ipynb`: Notebook for training the models.
  - `testing.ipynb`: Notebook for evaluating the models' performance.
  - `plot.ipynb`: Notebook for generating visualizations, such as confusion matrices and accuracy plots.

- **reports/**
  - Contains visual reports and result files.
  - `Confusion Matrix.png`: Image showing the confusion matrix of model predictions.
  - `Histogram of Confused Classes.png`: Image visualizing the most confused classes.
  - `best_model_result.csv`: CSV file with the results of the best-performing model.
  - `label_counts.csv`: CSV file containing counts of each label in the dataset.

- **scripts/**
  - Python scripts for data preprocessing and analysis.
  - `counting_labels.py`: Script for counting the number of occurrences of each label in the dataset.
  - `data_transformation.py`: Script for applying data transformations to the dataset.
  - `save_to_csv.py`: Script for saving the processed data to CSV format.
