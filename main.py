from fastapi import FastAPI, Response
import textwrap

app = FastAPI()

@app.get("/unit1")
def unit1():
    return Response(
        content=textwrap.dedent("""
        # Unit - 1 : Python code for Matrix Multiplication
        import numpy as np

        print("Matrix Multiplication:")

        # Input the size of square matrices
        n = int(input("\nEnter the size of the square matrices (n x n): "))

        # Input elements for Matrix A
        print("\nEnter elements (space separated) for Matrix A:")
        A = []
        for i in range(n):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        A.append(row)
        A = np.array(A)

        # Input elements for Matrix B
        print("\nEnter elements (space separated) for Matrix B:")
        B = []

        for i in range(n):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        B.append(row)
        B = np.array(B)

        # Multiply A and B
        result_multiplication = np.dot(A, B)

        # Print the result
        print(f"\nResult of Matrix Multiplication:\n{result_multiplication}")

                                

        # Unit 1 - Python code for inverse of matrix
        print("Matrix Inversion:")

        # Input the size of the square matrix
        m = int(input("\nEnter the size of the square matrix (m x m): "))

        # Input elements for the matrix
        print("\nEnter elements (space separated) for the matrix:")
        M = []
        for i in range(m):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        M.append(row)
        M = np.array(M)

        # Compute and print inverse
        try:
        inverse_M = np.linalg.inv(M)
        print(f"\nResult of Inverse of the Matrix:\n{inverse_M}")
        except np.linalg.LinAlgError:
        print("Matrix is singular and cannot be inverted.")
        """).strip(),
        media_type="text/plain",
        headers={"Cache-Control": "no-store"}
    )

@app.get("/unit2")
def unit2():
    return Response(
        content=textwrap.dedent("""
        # Unit 2 - Compute inner product of vectors (1,2,3) and (4,5,6).
        # Define the vectors
        u = [1, 2, 3]
        v = [4, 5, 6]
        # Compute the dot product
        dot_product = 0
        for i in range(len(u)):
            dot_product += u[i] * v[i]
        print(dot_product)


                                                                  
        # Unit 2 -  Check Orthogonality of vectors (2,-3,1) and (3,2,-6) using Python code
        # Define the vectors
        u = (2, -3, 1)
        v = (3, 2, -6)
        # Initialize dot product
        dot_product = 0
        # Iterate through each element
        for i in range(len(u)):
            dot_product += u[i] * v[i]
        # Check orthogonality
        if dot_product == 0:
            print("The vectors are orthogonal.")
        else:
            print("The vectors are NOT orthogonal.")
        """).strip(),
        media_type="text/plain",
        headers={"Cache-Control": "no-store"}
    )

@app.get("/unit3")
def unit3():
    return Response(
        content=textwrap.dedent("""
        Unit 3 - Use R code to construct scatter plots
        x <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        y <- c(2, 4, 6, 8, 10, 12, 15, 16, 18, 20);

        plot(x, y,
            main = "Scatter plot of x vs y",
            xlab = "X values",
            ylab = "y values",
            pch = 19,
            col = "blue")

                                

        # Unit 3 - If x= 1,2,3,4,5,6,7,8,9,10 ; y=2,4,5,7,10,12,15,16,18,20 , calculate Karl Pearson's coefficient of correlation using: i) Short cut method
        X <- c(10, 20, 30, 40, 50)
        Y <- c(20, 25, 28, 35, 40)

        n <- length(X)
        sumX <- sum(X)
        sumY <- sum(Y)
        sumX2 <- sum(X^2)
        sumY2 <- sum(Y^2)
        sumXY <- sum(X*Y)

        r <- (n * sumXY - sumX * sumY) / 
        sqrt((n * sumX2 - sumX^2) * (n * sumY2 - sumY^2))

        cat("Karl Pearson's coefficient of correlation (r) = ",r,"\n")
                                
        
                                
        # Unit 3 - Binomial Distribution
        # Data 
        X <- 0:6
        obs <- c(6, 37, 94, 125, 94, 38, 6)
        n <- 6
        N <- sum(obs)   # total observations

        # Estimate p
        mean_X <- sum(X * obs) / N
        p_hat <- mean_X / n

        # Expected frequencies
        exp_freq <- dbinom(X , size = n, prob = p_hat) * N

        # Result table
        result <- data.frame(success = X , observed = obs, expected =round(exp_freq, 4))
        print(result)

        # Chi square statistic
        chisq_val <- sum((obs - exp_freq)^2 / exp_freq)
        cat("Chi-square statistic = ", round(chisq_val, 4), "\n")
        """).strip(),
        media_type="text/plain",
        headers={"Cache-Control": "no-store"}
    )

@app.get("/unit4")
def unit4():
    return Response(
        content=textwrap.dedent("""
        # Unit 4 - estimating the parameters of some discrete and continuous probability distributions.
        # Sample Poisson data
        set.seed(123)
        data_pois <- rpois(50, lambda = 4)

        # Estimate lambda using sample mean 
        lambda_hat <- mean(data_pois)
        cat("Estimated lambda (Poisson):", lambda_hat, "\n")

        # Using fitdistr
        library(MASS)
        fit_pois <- fitdistr(data_pois, "Poisson")
        cat("MLE lambda using fitdistr:", fit_pois$estimate, "\n")

        """).strip(),
        media_type="text/plain",
        headers={"Cache-Control": "no-store"}
    )

@app.get("/unit5")
def unit5():
    return Response(
        content=textwrap.dedent("""
        # Unit 5 - Constructing Variance Covariance Matrix
        # Sample data: 3 variables (x1, x2, x3) with 5 observations
        data <- data.frame(
        x1 = c(2, 4, 6, 8, 10),
        x2 = c(1, 3, 5, 7, 9),
        x3 = c(10, 20, 30, 40, 50)
        )

        # Construct variance - covariance matrix
        var_cov_matrix <- cov(data)

        print("Variance - Covariance Matrix:")
        print(var_cov_matrix)
                                


        # Unit 5 - Principle Component Analysis.
        # Load built - in iris dataset
        data <- iris[, 1:4]

        # Run PCA
        pca <- prcomp(data, scale. = TRUE)

        # Print summary
        print(summary(pca))

        # Print loadings (eigenvectors)
        print(pca$rotation)

        # Print scores (new coordinates)
        head(pca$x)
                        

                                

        # Unit 5 - Estimated Covariance Matrix
        # Step 1: Create the data matrix x
        x <- as.matrix(iris[, 1:4])

        # Step 2: Estimate the mean vector (MLE for )
        mu_hat <- colMeans(x)
        print("Estimated Mean Vector (mu_hat):")
        print(mu_hat)

        # Step 3: Estimate the covariance matrix (MLE for )
        n <- nrow(x)
        p <- ncol(x)

        Sigma_mle <- t(x - matrix(mu_hat, n, p, byrow = TRUE)) %*%
                        (x - matrix(mu_hat, n, p, byrow = TRUE)) / n

        print("Estimated Covariance Matrix (Sigma_mle):")
        print(Sigma_mle)

        """).strip(),
        media_type="text/plain",
        headers={"Cache-Control": "no-store"}
    )

@app.get("/")
def home():
    return Response(
        content=textwrap.dedent("""
        tari masi no piko
        """).strip(),
        media_type="text/plain",
        headers={"Cache-Control": "no-store"}
    )
