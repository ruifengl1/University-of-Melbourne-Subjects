<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD007 -->
<!-- markdownlint-disable MD026 -->
<!-- markdownlint-disable MD040 -->
<!-- markdownlint-disable MD024 -->

# Statistical Machine Learning

## Contents

- [Introduction Probability Theory](#Introduction-Probability-Theory)
- [Statistical Schools of Thought](#Statistical-Schools-of-Thought)

---

## Introduction Probability Theory

- Data = raw information
- Knowledge = patterns or models behind the data

### Terminology

- **Instance**: _measurements_ about individual entities/objects.It is object that a model will be learned for prediction.
- **Attribute (Feature)**: component of the instances.
- **Label (Response)**: an outcome that is categorical, numeric, etc(after prediction).
- **Models**: discovered relationship between attributes and/or label

### Supervised vs unsupervised learning

In _supervised learning_, Input and output data are labelled for classification to provide a learning basis for future data processing.

In _unsupervised learning_, an AI system is presented with unlabeled, uncategorised data and the system’s algorithms act on the data without prior training. The output is dependent upon the coded algorithms.

### Evaluation (supervised learners)

- Typical process, Pick an _evaluation metric_
- When data poor, _cross-validate_

## Statistical Schools of Thought

### Frequentist Statistics

- _parameter_:  a value that tells you something about a entire population and something in an equation that is passed on in an equation. A parameter never changes, because everyone (or everything) was surveyed to find the parameter. For example, the average age of everyone in your class is a parameter.
- _parameter estimates_: Parameters are descriptive measures of an entire population. However, their values are usually unknown because it is infeasible to measure an entire population. Because of this, you can take a random sample from the population to obtain parameter estimates. One goal of statistical analyses is to obtain estimates of the population parameters along with the amount of error associated with these estimates.
- _Point estimate_: Point estimates are the single, most likely value of a parameter. For example, the point estimate of population mean (the parameter) is the sample (100 out of entire population) mean (the parameter estimate).
- The difference between _a statistic and a parameter_ is that statistics describe a sample. A parameter describes an entire population.

To estimate good behaviour in ideal conditions:

- _Bias_: The error due to bias is taken as the difference between the expected (or average) prediction of our model and the correct value which we are trying to predict. We have only one model so talking about expected or average prediction values might seem a little strange, but we can use the whole process more than once. _Bias measures how for off in general these models predictions are from the correct value._
- _Variance_: The error due to variance is taken as the variability of a model prediction for a given data point.The variance is how much the predictions for a given point vary between different realization of the model.

Asymptotic properties (it is typically assumed that the sample size n grows indefinitely):

- _Consistency_: Estimates converges to true value as the number of data points used increases indefinitely.
- _Efficiency_: asymptotic variance is as small as possible as the number of data points used increases indefinitely.

#### Maximum‐Likelihood Estimation

It is a method in statistics for estimating parameter(s) of a model for given data. The basic intuition behind MLE is that the estimate which explains the data best, will be the best estimator. The main advantage of MLE is that it has asymptotic property. It means that when the size of the data increases, the estimate converges faster towards the population parameter

- It is a _general principle_ for designing estimators or machine learning algorithms
- Involves optimisation
- MLE estimators are consistent (under technical conditions)
<img src="images/MLE.png" alt="350" width="350">

### Statistical Decision Theory

- _Decision rule_: A decision rule is a procedure that the researcher uses to decide whether to accept or reject the null hypothesis. For example, a researcher might hypothesize that a population mean is equal to 10. He/she might collect a random sample of observations to test this hypothesis. The decision rule might be to accept the hypothesis if the sample mean were close to 10 (say, between 9 and 11), and to reject the hypothesis if the sample mean were not close to 10 (say, less than 9 or greater than 11).
- _Loss function_: a loss function quantifies the losses associated to the errors committed while estimating a parameter. Often the expected value of the loss, called statistical risk, is used to compare two or more estimators: in such comparisons, the estimator having the least expected loss is usually deemed preferable.

#### Bias‐variance decomposition

The bias-variance decomposition is a useful theoretical tool to understand the performance characteristics of a learning algorithm.The decomposition allows us to see that the mean squared error of a model (generated by a particular learning algorithm) is in fact made up of two components. The bias component tells us how accurate the model is, on average across different possible training sets. The variance component tells us how sensitive the learning algorithm is to small changes in the training set

<img src="images/Bias‐variance decomposition.png" alt="350" width="350">

#### Empirical Risk Minimisation (ERM)

When we build our learning model, we need to pick the function that minimizes the empirical risk i.e. the delta between the predicted output and the actual output for the data points in our dataset. This process of finding this function is called empirical risk minimization. Ideally, we would like to minimize the true risk. But we don’t have the information that allows us to achieve that, so our hope is that this empiricial risk will almost be the same as the true empirical risk. Hence by minimizing it, we aim to minimize the true risk.

<img src="images/ERM.png" alt="350" width="350">

** average(1/n) in the above equation

### Bayesian Statistics

- _Beliefs_: beliefs are encode as distributions in Bayesian learning

 <img src="images/beliefs.png" alt="350" width="350">

**Bayesian statistics** is a mathematical procedure that applies probabilities to statistical problems. It provides people the tools to update their beliefs in the evidence of new data.

 <img src="images/Bayesian_ML.png" alt="550" width="550">

 <img src="images/bayesian_machine_learning.png" alt="450" width="450">

**Frequentist Statistics** tests whether an event (hypothesis) occurs or not. It calculates the probability of an event in the long run of the experiment (i.e the experiment is repeated under the same conditions to obtain the outcome). Here, the sampling distributions of fixed size are taken. Then, the experiment is theoretically repeated infinite number of times but practically done with a stopping intention. For example, I perform an experiment with a stopping intention in mind that I will stop the experiment when it is repeated 1000 times or I see minimum 300 heads in a coin toss.
