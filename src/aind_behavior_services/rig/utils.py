import numpy as np
from numpy.typing import ArrayLike


class LinearRegression:
    """
    Simple linear regression implementation maintaining some of sklearn's interface.

    Fits a linear model with coefficients to minimize the residual sum of squares
    between the observed targets in the dataset, and the targets predicted by the
    linear approximation.

    Attributes:
        coef_ (np.ndarray): Estimated coefficients for the linear regression problem.
        intercept_ (float): Independent term in the linear model.
    """

    def __init__(self, fit_intercept: bool = True, positive: bool = False) -> None:
        self.fit_intercept = fit_intercept
        self.positive = positive
        self.coef_: np.ndarray | None = None
        self.intercept_: float | None = None
        self._X_train: np.ndarray | None = None
        self._y_train: np.ndarray | None = None

    def fit(self, X: ArrayLike, y: ArrayLike) -> "LinearRegression":
        X = np.asarray(X)
        y = np.asarray(y)

        if X.ndim == 1:
            X = X.reshape(-1, 1)

        self._X_train = X
        self._y_train = y

        if self.fit_intercept:
            X_with_intercept = np.c_[np.ones(X.shape[0]), X]
            coefficients = np.linalg.lstsq(X_with_intercept, y, rcond=None)[0]
            self.intercept_ = coefficients[0]
            self.coef_ = coefficients[1:]
        else:
            coefficients = np.linalg.lstsq(X, y, rcond=None)[0]
            self.intercept_ = 0.0
            self.coef_ = coefficients

        if self.positive:
            assert self.coef_ is not None
            self.coef_ = np.maximum(self.coef_, 0)
            if self.fit_intercept:
                assert self.intercept_ is not None
                self.intercept_ = max(self.intercept_, 0)

        return self

    def predict(self, X: ArrayLike) -> np.ndarray:
        if self.coef_ is None or self.intercept_ is None:
            raise ValueError("Model has not been fitted yet. Call fit() first.")

        X = np.asarray(X)

        if X.ndim == 1:
            X = X.reshape(-1, 1)

        return self.intercept_ + X @ self.coef_

    def score(self, X: ArrayLike, y: ArrayLike) -> float:
        """
        Return the coefficient of determination R² of the prediction.

        Args:
            X: Test samples.
            y: True values for X.

        Returns:
            R² score.
        """
        y = np.asarray(y)
        y_pred = self.predict(X)
        ss_res = np.sum((y - y_pred) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        return 1 - (ss_res / ss_tot)
