
"""
This module defines the following routines used by the 'train' step of the regression pipeline:

- ``estimator_fn``: Defines the customizable estimator type and parameters that are used
  during training to produce a model pipeline.
"""

from mlflow.pipelines.decorators import mlp


@mlp
def estimator_fn():
    """
    Returns an *unfitted* estimator that defines ``fit()`` and ``predict()`` methods.
    The estimator's input and output signatures should be compatible with scikit-learn
    estimators.
    """
    from sklearn.linear_model import SGDRegressor

    return SGDRegressor(random_state=43)
