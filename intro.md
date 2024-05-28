## What is the Iris dataset?

The Iris dataset, also called the Iris flower dataset, is a multivariate dataset used by Ronald Fisher, a famous British statistician and biologist, in his [1936 paper \[1\]](#references). He used the data to present linear discriminant analysis.

Ever since, the dataset has been used by plenty researchers - interestingly, not biologists, as it contains rather quite basic data about the Iris species, but by authors who used it to present various numerical techniques in multivariate statistics, pattern recognition and visualization.

The dataset is also provided as an example dataset in various software, including [R](https://rpubs.com/moeransm/intro-iris) and [`scikit-learn`](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html).

## Origin

While the dataset was popularized by Fisher, the data themselves originated from the article by [Edgar Anderson \[2\]](#references), who studied morphologic variations in Iris flowers of three species, _Iris setosa_, _I. versicolor_ and _I. virginica_.

## Issues with the data

### Errors in the dataset?

[Bezdek et al. \[3\]](https://lucykuncheva.co.uk/papers/jbjkrklknptfs99.pdf) discussed that there have been several errors incorporated to the original dataset. Therefore, you should be cautious to use the correct dataset. They write,

> During the writing of this book we have discovered (perhaps others have known this for a long time, but we did not) that there are at least two (and, hence, probably half a dozen) different well-publicized versions of Iris.

They specify these errors:

> Specifically, vector 90, class 2 (Iris Versicolor) in Iris has the coordinates (5.5, 2.5, 4, 1.3) in Johnson and Wichern [5, p. 566] and has the coordinates (5.5, 2.5, 5, 1.3) in Chien [6, p. 224].

Note that the first coordinates from this sentence are correct while the other aren't. (See the references to Johnson and Wicher under [4] and to Chien under [5] [in the Refernces sectoin](#references).)

Bezdek et al. wrote this 25 years ago... Has the situation changed? Have more versions of the Iris dataset appeared? Did this affect the development of various numerical methods in which the data were used? That's an open question - and feel free to address it in your research.

This dashboard offers you an opportunity to play with the Iris data, in order to check by yourself whether the general picture that the data shows is affected by such small changes. Go to the `Play with the data` tab and incorporate any changes to the Iris dataset and find yourself whether they make a difference.


### Do irises have sepals at all?

This time, it's a biological issue. Kozak and Lotocka [6] raise a question whether Iris flowers... do have sepals whatsoever! They cite authors who botanists who claim that Iris flowers do have sepals and authors who claim otherwise.

They write:

> In the few monocots having petaloid tepals that have been studied (Iris was not among them), the B-class domain is extended to encompass both whorls of perigon [14]. Therefore, in molecular terms such monocots have only petals in their perigon. In the other monocots the molecular background of sepaloid perigon formation is
not clear.

(You'll find the reference under [7] in [the references](#references))

Kozak and Lotocka [6] write,

> Hopefully, the molecular mechanisms underlying the formation of sepals and petals or tepals will provide less arbitrary classification criteria.

It'd be nice to finally learn the truth, wouldn't it? From a botanical point of view, this is a serious issue. While this won't affect any of the conclusions that all the statisticians, data scientists and pattern recognition scientists draw based on this data, I guess you'll agree that the meaning of the dataset would change if it occurred that Iris flowers do not have sepals at all.

Since the knowledge develops so quickly, I am sure that we'll learn the truth sooner or later. Maybe botanists already do? If this is the case, they should share it with all those who don't know all that much about botany and Iris flowers but who do use the Iris dataset so extensively.


## References

1. R.A. Fisher (1936). The use of multiple measurements in taxonomic problems. _Annals of Eugenics_, 7(2): 179-188. doi:10.1111/j.1469-1809.1936.tb02137.x.
2. E. Anderson (1935). The irises of the Gaspe Peninsula. _Bulletin of the American Iris Society_, 59: 2-5.
3. J.C. Bezdek, J.M. Keller, R. Krishnapuram, L.I. Kuncheva, N.R. Pal (1999). Will the real iris data please stand up?. _IEEE Transactions on Fuzzy Systems_, 7(3): 368-369.
4. R. A. Johnson and D. W. Wichern (1992) _Applied Multivariate Statistical Analysis_. 3rd ed. Englewood Cliffs, NJ: Prentice-Hall.
5. Y.T. Chien (1978). _Interactive Pattern Recognition_. Monticello, NY: MarcelDekker.
6. M. Kozak, B. Lotocka (2013). What should we know about the famous Iris data. _Current Science_, 104(5): 579-580.
7. A. Kanno, H. Saeki, T. Kameya, H. Saedler, G. Theissen (2003). Heterotopic expression of class B floral homeotic genes supports a modified ABC model for tulip (Tulipa gesneriana). _Plant Molecular Biology_, 52, 831-841.