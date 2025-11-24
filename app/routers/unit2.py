from fastapi import APIRouter

router = APIRouter()

@router.get("/")
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