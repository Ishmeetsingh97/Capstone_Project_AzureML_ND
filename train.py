import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from argparse import ArgumentParser
from azureml.core.run import Run
import os
import joblib

data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
data.columns =['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'iris_class'] 

x=data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y=data[['iris_class']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)
run = Run.get_context()


def main():
    parser = ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength.")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge.")

    args = parser.parse_args()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))
    os.makedirs('outputs', exist_ok=True)

    joblib.dump(value=model, filename='outputs/model.pkl')

if __name__ == '__main__':
    main()
