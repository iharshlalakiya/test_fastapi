from fastapi import FastAPI

app = FastAPI()

@app.get("/unit1")
def unit1():
    r_code = """
    is_prime <- function(n) {{
    if (n < 2) return(FALSE)
    if (n == 2) return(TRUE)
    if (n %% 2 == 0) return(FALSE)
    for (i in seq(3, floor(sqrt(n)), by=2)) {{
        if (n %% i == 0) return(FALSE)
    }}
    TRUE
    }}

    primes_up_to <- function(limit) {{
    which(sapply(1:limit, is_prime))
    }}

    primes_up_to({limit})
    """
    return {"r_code": r_code}

@app.get("/unit2")
def unit2():
    r_code = """
    is_prime <- function(n) {{
    if (n < 2) return(FALSE)
    if (n == 2) return(TRUE)
    if (n %% 2 == 0) return(FALSE)
    for (i in seq(3, floor(sqrt(n)), by=2)) {{
        if (n %% i == 0) return(FALSE)
    }}
    TRUE
    }}

    primes_up_to <- function(limit) {{
    which(sapply(1:limit, is_prime))
    }}

    primes_up_to({limit})
    """
    return {"r_code": r_code}

@app.get("/unit3")
def unit3():
    r_code = """
    is_prime <- function(n) {{
    if (n < 2) return(FALSE)
    if (n == 2) return(TRUE)
    if (n %% 2 == 0) return(FALSE)
    for (i in seq(3, floor(sqrt(n)), by=2)) {{
        if (n %% i == 0) return(FALSE)
    }}
    TRUE
    }}

    primes_up_to <- function(limit) {{
    which(sapply(1:limit, is_prime))
    }}

    primes_up_to({limit})
    """
    return {"r_code": r_code}

@app.get("/unit4")
def unit4():
    r_code = """
    is_prime <- function(n) {{
    if (n < 2) return(FALSE)
    if (n == 2) return(TRUE)
    if (n %% 2 == 0) return(FALSE)
    for (i in seq(3, floor(sqrt(n)), by=2)) {{
        if (n %% i == 0) return(FALSE)
    }}
    TRUE
    }}

    primes_up_to <- function(limit) {{
    which(sapply(1:limit, is_prime))
    }}

    primes_up_to({limit})
    """
    return {"r_code": r_code}

@app.get("/unit5")
def unit5():
    r_code = """
    is_prime <- function(n) {{
    if (n < 2) return(FALSE)
    if (n == 2) return(TRUE)
    if (n %% 2 == 0) return(FALSE)
    for (i in seq(3, floor(sqrt(n)), by=2)) {{
        if (n %% i == 0) return(FALSE)
    }}
    TRUE
    }}

    primes_up_to <- function(limit) {{
    which(sapply(1:limit, is_prime))
    }}

    primes_up_to({limit})
    """
    return {"r_code": r_code}

@app.get("/")
def home():
    return {"message": "tari masi no piko"}
