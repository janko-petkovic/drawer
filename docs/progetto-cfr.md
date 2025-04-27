# Progetto con Catarina, Ferdinando e Rita

Question: does the addition of manually designed directional filters improve the classification performance of LeNet-5 on MNIST images occluded with a grating, without the need for a previous training with data augmentation?



## Methods

Dataset: MNIST, occMNIST (occluded MNIST)

Model: LN5, FLN5 (filterLeNet-5,  im bad with names)



### Train-test loops

We defined the followting pipelines (both for LN5 and FLN5):

1. Base loop: train MNIST, test MNIST

2. Augmented loop: train occMNIST, test occMNIST

3. Generalization loop: train MNIST, test occMNIST



### Model selection

#### Defining the hyperparameters

To investigate our question, we have to select the the best performing FLN5. Practically, this means selecting which manual filters are to be added to LN5. To this end, we have to tune two parameters: the filter kernel size (size of the filter in pixels) and "filtering width" (the width in pixels of the white stripe).

*We have altrady seen that filters of dimension 3 do not work well, probably due to the fact that the digits in MNIST are too thick [Rita and Aneeqa].*

How do we select the best hyperparameters? A grid search looks like a reasonable choice. For the grid search, we can use the following values:

1. kernel size: from 4 to 14 pixels (half the width of a MNIST image - remember the role of parasol cells in the eye, each covering extensive portions of the retina).

2. filtering width: this clearly has to vary in function of the filter size. A spanne, we could go from 1 pixel to 1/3 of the kernel size. 

Since (ideally) we want the filter stripes to traverse the center of the filter, we'd only try filters with odd kernel sizes (this is, of course, amendable, at the cost of some additional coding). Up until here, we should have a total number N of grid elements  

$$
N = \sum_{i=2}^{7} \sum_{j=1}^{\lfloor (2i+1)/3 \rfloor}1 = 18 \quad \text{(if I'm not mistaken)}
$$

which can be easily explored in more or less half an hour. It seems that we have space for a third, possibly important, hyperparameter:

3. the number of filters is also a hyperparameter and it also would depend on the kernel size.

For example, with kernel size = 5, width=1, we have 4 different filters. When the size is bigger, however, not only we have more possible orientations, but using all of them is not guaranteed to be the optimal solution.

For a given kernel size $s \in \mathbb{N}$, the number of possible different orientations should be $2(s-1)$ (each orientation is a straight line going through the center and ending at a different edge pixel). For a kernel size of 15, this means 28 different orientations (and filters).

Now, which filters do we include in the model? Who guarantees that the best choice of filters is one uniformly covering all the orientations? Maybe due to the featuers of the MNIST dataset, we want to take multiple filters around 45 degrees and only one at 135 degrees (maybe also not though).

For a given $s$, the total number of filter combinations should be $2^{2(s-1)}$. It looks therefore unfeasible to grid search everything. Two options are possible:

1. we only consider filter sets with uniform angle coverage - V1 shows no angular bias for orientation columns;

2. for a fixed number (which?) of filters, we randomly sample some groups (how many? is there an optimal way? can we use bayesian methods - Optuna? [1])

If we go for uniform orientation coverage, the total number of possible filter configurations (starting from a minimum of 4 filters) should be $\frac{s-3}{2}+1$. This translates to a total number of grid search elements of 

$$
N = \sum_{i=2}^{7} \sum_{j=1}^{\lfloor (2i+1)/3 \rfloor} \sum_{k=1}^{i} 1 
= \sum_{i=2}^{7} i \sum_{j=1}^{\lfloor (2i+1)/3 \rfloor} 
= 94
$$

(again if I'm not making mistakes, which is very possible). This is still very feasible (2 hrs of runtime, tops). 

*Possible interesting finding to look out for:* maybe, we get that the best performing FLN5 has filter width comparable with the mean leading spatial frequency of the MNIST digits (is there some optimality that is granted? Some indetermination minimization? - cfr. considerations in [2]).



#### Tuning the hyperparameters

For the grid search introduced above, we use the validation performance as our goodness metric. This evaluation can be conducted via:

1. base loop: in my opinion the best choice. Only spatial scale factor in the training is the digit width in pixels, which allows us to speculate on the best filter width;

2. augmented loop: the biological columnar system has evolved in order to be able to solve the occlusion problem. One could argue that this is also how our hyperparameters should be tuned, considering the occlusion problem at hand. The disadvantages are:
   
   - the final filter width could be related both to the digit and the occlusion widths;
   
   - it is unclear (to me) if the grid search should be conducted for each occlusion width (in this case, a total of $14 \cdot 94 = 1316$ runs should be conducted, which is still feasible - 2 days of runtime tops);
   
   - it is unclear (to me) how the final testing on the "generalization loop" should be interpreted

A third way would be using directly the generalization loop for model selection, but that should be something we are testing with at the end, not training with. 

Althought, from an observational point of view, one could do it and then limit the work to post-hoc speculation without claiming any proofs. Again, it would be unclear how to do the grid search in function of the occlusion widths.



## (Possible) results

### Collecting the results

After tuning the hyperparameters, we evaluate the test performance in function of the occlusion width of LN5 and fLN5 using the generalization loop. What we would love to see is that fLN5 performs better, strongly suggesting that the filters serve their purpose in completing occluded contours. Alternatively, do we acheive same performance but in half of the training time? That would also be something reasonably remarkable.

I personally think that, If we conducted the hyperparameter search using the base loop, analyzing the data coming from the augmented loop could also be interesting, since it could give some intuition on the "trainability" of LN5 and fLN5 on occlued images. Also, it could act as a (positive?) control condition.



### Explanation of the results

As far as I understood, if everything goes well and we get better performance and everything, we would love to see the actual border completion effect on the occlued images. This is not easy to show since our manual convolutional layer creates a number of hidden outputs, which are not easy to inspect visually. Maybe we could recur to the ideas presented Bertoni's - or Montobbios' - thesis (I have no references to it though, maybe Rita has).

Another thing. Once the pipeline is set up, it should have no implementational cost to rerun it from top to bottom for FashionMNIST, or other, **black and white** datasets. Maybe we want also to consider this.



References

[1] https://optuna.readthedocs.io/en/stable/index.html

[2] Marr, D.C., & Hildreth, E.C. (1979). Theory of edge detection. *Proceedings of the Royal Society of London. Series B. Biological Sciences, 207*, 187 - 217.


