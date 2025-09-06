# [Statistical notes on misspec](https://www.statlect.com/glossary/model-misspecification)

### Problems often mislabeled as misspecification

As we said above, several important problems are often incorrectly considered
 misspecification problems.

For example:

- **Omitted variable bias**: due to the exclusion of some
   regressors, the regression coefficients do not have a causal interpretation
   (e.g., [Angrist and Pischke 2009](https://www.statlect.com/glossary/model-misspecification#Angrist)).

- **Irrelevant regressors**: due to the presence of many regressors
   that are unlikely to be correlated with the dependent variable, the OLS
   estimators of the regression coefficients have high variance.

- **Inappropriate functional form**: **by formulating a different
   regression model (where the variables are transformed through nonlinear
   functions), the variance of the error terms would decrease considerably.**

When these problems are present, there may exist a better regression model
 than the one we have chosen. For example, a different model may be more
 interpretable, easier to estimate precisely, or it may produce better
 forecasts.

But **the fact that we can improve our model in some respect does not
 mean that our model is misspecified**. In other words, all of the
 assumptions we have made may still be satisfied by the data-generating
 distribution.

[Spanos (2011)](https://www.statlect.com/glossary/model-misspecification#Spanos) provides one of the most articulated
 discussions about this point, where he clearly distinguishes between:

- statistical adequacy (i.e., the lack of misspecification);

- substantive adequacy (i.e., the lack of significant opportunities to improve
   the model).

**What is our issue in neuroscience? Mainly wrong models! How can we also improve the data generating process? Can we train a neural network to produce reality-like data parametrizing it as a black box?**

# Model Misspecification in Simulation-Based Inference - Recent Advances and Open Challenges

Problem: assume that the the joint (dependent/independent) is a true
representation of reality. 



Bayesian inference with misspecified models - Stephen G. Walker

Foundational Issues in Statistical Modeling: Statistical Model Specification and Validation
