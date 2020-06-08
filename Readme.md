# Matrix Experiment

<img align="right" width="300px" src="./media/header.png">

> "The Scientific Method"

In this experiment I ran some tests on matrix multiplication and wrote up the results in a report to document my findings. 

# Resources 

Provided below are a list of curated resources that helped me complete the experiment. 

1. Matrix Multiply
	- [https://www.mathsisfun.com/algebra/matrix-multiplying.html](./https://www.mathsisfun.com/algebra/matrix-multiplying.html)
2. Compiling code in C
	- [http://courses.cms.caltech.edu/cs11/material/c/mike/misc/compiling_c.html](http://courses.cms.caltech.edu/cs11/material/c/mike/misc/compiling_c.html)
3. Compiling Java code
	- [https://www.cs.swarthmore.edu/~newhall/unixhelp/debuggingtips_Java.html](https://www.cs.swarthmore.edu/~newhall/unixhelp/debuggingtips_Java.html)

# Task 1 - Matrix Multiply

## The goal

The goal is to run several experiments on matrix multiply using a few different languages and configurations. Very small changes can effect performance.

## The report

Included in this part is a [Report.odt](./Report.odt) where I documented my results. 

## Step 1 - Experimental Setup 

Documented in the report is my experimental setup. Some helpful commands to gather my machine specifications that were run in the terminal are the following:

```
lscpu - to display information about the CPU architecture
lspci - to list all PCI devices
```

I also ran [Stabilizer](./https://github.com/ccurtsinger/stabilizer) for the compiled code. 

```
# Example
szc -Rcode -Rstack -Rheap matrix.c -o matrix
```

### Other parameters

For all of my experiments, I used a matrix size of 1024x1024. 

## Step 2 - Java

Java itself compiles to bytecode, and then it *may* compile during run-time through the Java virtual machine into native machine code. I wanted to test the performance of Java to also see how it compares.

In [./experiments/matrix.java](./experiments/matrix.java) I implemented matrix multilpy in Java. 

## Step 3 - Compile-Time initialization (Using Meta-Programming)

There is another optimization which may often result in a performance boost. Instead of spending time during run-time computing results, and potentially altering the cache, we can pre-compute values at compile-time and store them in our binary. More often we just think of this as [initialization](https://webhome.phy.duke.edu/~rgb/General/c_book/c_book/chapter6/initialization.html) of values.

As an example:

```
    // Initialize array
    for(int i =0; i < N; ++i){
        for(int j =0; j < N; ++j){
            A[i][j] = (double)rand() / (double)RAND_MAX;
            B[i][j] = (double)rand() / (double)RAND_MAX;
            C[i][j] = 0; // This could be pre-computed and stored above our 'main'
        }
    }
```

We could instead initialize our 'C' array ahead of time like such:

```
int C[1024][1024] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ....};
```

It may be 'annoying' to type out 1024 x 1024 zeroes, so sometimes programmers use a technique known as [meta-programming](https://cs.lmu.edu/~ray/notes/metaprogramming/) to write a program that outputs other source code. To generate a valid C-string that I could paste into C code such that it compiles, I wrote tools and included them above.

I then implemented another program called [./experiments/matrix_meta.c](./experiments/matrix_meta.c) that initializes the values during compile-time.

## Step 4 - Running the experiments

From here I now had the following programs to run:

1. [./experiments/matrix.c](./experiments/matrix.c)	
2. [./experiments/matrix.java](./experiments/matrix.java)	
3. [./experiments/matrix.py](./experiments/matrix.py)	
4. [./experiments/matrix_meta.c](./experiments/matrix_meta.c)	
5. [./experiments/matrix_order.c](./experiments/matrix_order.c)

I ran each program '30' times, where '30' is the number of trials. I wrote a script to do so, such that I could run one trial after the other, and then record the results. I also summarized these results in a table in [Report.odt](./Report.odt).
