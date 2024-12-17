
"morphologicalOperation.py"

In this script i've implemented a morphological operation on a binary image 
It's based on 'majority' operation from MathWorks (2024)
The script analyses 3x3 neighborhood; if there are 5 or more
pixels equal to 1 around the central pixel; it changes its value 
to 1; otherwise, the central pixel will be 0 

n is the number of times the algorithm will be applied on the image
I recomend 10 times (n=10)


$$\begin{bmatrix}
	1&1&1\\
	1&\text{\textcolor{purple}{\textbf{0}}}&0\\
	0&1&1
\end{bmatrix}
\Longrightarrow
\begin{bmatrix}
	1&1&1\\
	1&\text{\textcolor{purple}{\textbf{1}}}&0\\
	0&1&1
\end{bmatrix}$$
