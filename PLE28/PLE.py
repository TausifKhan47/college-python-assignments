from plotnine.data import economics

print(economics)

from plotnine import ggplot, aes, geom_line

(
    ggplot(economics)  # What data to use
    + aes(x="date", y="pop")  # What variable to use
    + geom_line()  # Geometric object to use for drawing
)
from plotnine.data import mpg
from plotnine import ggplot, aes, geom_point

ggplot(mpg) + aes(x="class", y="hwy") + geom_point()
