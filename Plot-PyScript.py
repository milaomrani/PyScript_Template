<html>

<head>
    <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
    <py-env>
        - numpy
        - matplotlib
    </py-env>
</head>

<body>
<h1>My Plot from matplotlib</h1>
<div id="plot"></div>
<p>Let plot random #</p><br>
<py-script output="plot">
import matplotlib.pyplot as plt
import numpy as np


# generate some int values
value = np.random.randint(0, 15, 1000)

fig, ax = plt.subplots()
ax.hist(value, bins=10)
fig

</py-script>

</body>
</html>
