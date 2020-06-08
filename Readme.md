# Part 2 - Matrix Experiment

<img align="right" width="300px" src="./media/header.png">

> "The Scientific Method"

In this part you are going to exercise the scientific method that you may be utilizing now, or have learned long ago! You are going to run some experiments on matrix multiplication and write up the results in a report to document your findings. 

# Resources to help

Provided below are a list of curated resources to help you complete the task(s) below. Consult them (read them, or do ctrl+f for keywords) if you get stuck.

1. Matrix Multiply
	- [https://www.mathsisfun.com/algebra/matrix-multiplying.html](./https://www.mathsisfun.com/algebra/matrix-multiplying.html)
2. Compiling code in C
	- [http://courses.cms.caltech.edu/cs11/material/c/mike/misc/compiling_c.html](http://courses.cms.caltech.edu/cs11/material/c/mike/misc/compiling_c.html)
3. Compiling Java code
	- [https://www.cs.swarthmore.edu/~newhall/unixhelp/debuggingtips_Java.html](https://www.cs.swarthmore.edu/~newhall/unixhelp/debuggingtips_Java.html)

# Task 1 - Matrix Multiply

## The goal

The goal is to run several experiments on matrix multiply using a few different languages and configurations. Very small changes can effect performance, and we will want to report on those.

## The report

Included in this part is a [ReportTemplate.odt](./ReportTemplate.odt) where you will report on your results. The [ReportTemplate.odt](./ReportTemplate.odt) will walk you through the details of each section that you should fill out.

## Step 1 - Experimental Setup 

In the report, you will be documenting your experimental setup. Some helpful commands to gather your machine specifications that you may run on the terminal are the following:

```
lscpu - display information about the CPU architecture
lspci - list all PCI devices
```

You will also be running [Stabilizer](./https://github.com/ccurtsinger/stabilizer) for the compiled code examples. Stabilizer has been install on the virtual machine for you.

```
# Example
szc -Rcode -Rstack -Rheap matrix.c -o matrix
```

### Other parameters

For all of your experiments, use a matrix size of 1024x1024. You may increase the size of the matrix if you like, but 1024x1024 should be the minumum.

## Step 2 - Java

One key programming language we did not discuss in lecture was Java. Java itself compiles to bytecode, and then it *may* compile during run-time through the Java virtual machine into native machine code. We will want to test the performance of Java to also see how it compares.

In [./experiments/matrix.java](./experiments/matrix.java) implement matrix multilpy in Java. You may use additional compiler flags to try to improve the Java compiler as well, but make sure to include them in the report.

## Step 3 - Compile-Time initialization (Using Meta-Programming)

There is another optimization which we did not talk about which may often result in a performance boost. Instead of spending time during run-time computing results, and potentially altering the cache, we can pre-compute values at compile-time and store them in our binary. More often we just think of this as [initialization](https://webhome.phy.duke.edu/~rgb/General/c_book/c_book/chapter6/initialization.html) of values.

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

It may be 'annoying' to type out 1024 x 1024 zeroes, so sometimes programmers use a technique known as [meta-programming](https://cs.lmu.edu/~ray/notes/metaprogramming/) to write a program that outputs other source code. You may use any programming language you like to generate a valid C-string that you can paste into C code such that it compiles. **Include** this program in your submission.

Once you have done the above--implement another program called [./experiments/matrix_meta.c](./experiments/matrix_meta.c) that initializes the values during compile-time.

## Step 4 - Running the experiments

You now have the following programs to run:

1. [./experiments/matrix.c](./experiments/matrix.c)	
2. [./experiments/matrix.java](./experiments/matrix.java)	
3. [./experiments/matrix.py](./experiments/matrix.py)	
4. [./experiments/matrix_meta.c](./experiments/matrix_meta.c)	
5. [./experiments/matrix_order.c](./experiments/matrix_order.c)

Run each program '30' times, where '30' is the number of trials. I recommend writing a script to do so, such that you can run one trial after the other, and then record the results. You will summarize these results in a table in your [ReportTemplate.odt](./ReportTemplate.odt).

# Submission/Deliverables

### Submission

- Commit all of your files to github, including any additional files you create.
- Do not commit any binary files unless told to do so.
- Do not commit any 'data' files generated when executing a binary, but otherwise commit 'data' files you used for colleting results..

### Deliverables

- Fill out the [ReportTemplate.odt](./ReportTemplate.odt) with your results
- Your implementation of [./experiments/matrix.java](./experiments/matrix.java)
- Your implementation of [./experiments/matrix_meta.c](./experiments/matrix_meta.c)
- Your meta-programming script
- Any additional scripts to run your experiment
	- A good experiment is reproducible.

# Going Further

An optional task(if any) that will reinforce your learning throughout the semester--this is not graded.

1. Try another language like Rust or Go and see the results!

# F.A.Q. (Instructor Anticipated Questions)

1. Q: Can I write my report in LaTex?
	- A: Yes, please feel free to do so. Just make sure to upload the .pdf to this directory.
2. Q: Can I add more trials to the experiment?
	- A: Yes, please feel free to add more languages or other optimizations.
	- It may for instance be interesting to see if adding debug information (-g) speeds up or slows down the program in any way.
3. Q: Should I include any scripts or spreadsheets of the data I collected?
	- A: Yes please do.
