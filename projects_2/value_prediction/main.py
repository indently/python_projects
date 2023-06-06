from model import Prediction
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


def make_prediction(inputs: list[float], outputs: list[float], input_value: float, plot: bool = False) -> Prediction:
    if len(inputs) != len(outputs):
        raise Exception(f'Length of "inputs" & "outputs" must match')

    # Create a dataframe for our data
    df = pd.DataFrame({'inputs': inputs, 'outputs': outputs})

    # Reshape the data using Numpy (X: Inputs, y: Outputs)
    X = np.array(df['inputs']).reshape(-1, 1)
    y = np.array(df['outputs']).reshape(-1, 1)

    # Split the data into training data to test our model
    train_X, test_X, train_y, test_y = train_test_split(X, y, random_state=0, test_size=.20)

    # Initialize the model and test it
    model = LinearRegression()
    model.fit(train_X, train_y)

    # Prediction
    y_prediction = model.predict([[input_value]])
    y_line = model.predict(X)

    # Testing for accuracy
    y_test_prediction = model.predict(test_X)

    # Plot the data
    if plot:
        display_plot(inputs=X, outputs=y, y_line=y_line)

    # Return the data
    return Prediction(value=y_prediction[0][0],
                      r2_score=r2_score(test_y, y_test_prediction),
                      slope=model.coef_[0][0],
                      intercept=model.intercept_[0],
                      mean_absolute_error=mean_absolute_error(test_y, y_test_prediction)
                      )


def display_plot(inputs: list[float], outputs: list[float], y_line):
    plt.scatter(inputs, outputs, s=12)
    plt.xlabel('Inputs')
    plt.ylabel('Outputs')
    plt.plot(inputs, y_line, color='r')
    plt.show()


if __name__ == '__main__':
    # Create some sample data
    years: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    earnings: list[int] = [1000, 800, 2000, 1500, 3400, 3700, 4000, 3800, 5000, 4800]
    my_input: int = 15

    # Create a prediction
    prediction: Prediction = make_prediction(inputs=years, outputs=earnings, input_value=my_input, plot=False)
    print('Input:', my_input)
    print(prediction)
