# pylint: disable=pointless-statement

import myLib.data

train_set_x, train_set_y, test_set_x, test_set_y = myLib.data.injest()

logistic_regression_model = myLib.helper.model(
    train_set_x,
    train_set_y,
    test_set_x,
    test_set_y,
    num_iterations=2000,
    learning_rate=0.005,
    print_cost=True,
)