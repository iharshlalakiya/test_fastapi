from fastapi import FastAPI, Response
import textwrap

app = FastAPI()

@app.get("/unit1")
def unit1():
    return Response(
        content=textwrap.dedent("""
        is_prime <- function(n) {
          if (n < 2) return(FALSE)
          if (n == 2) return(TRUE)
          if (n %% 2 == 0) return(FALSE)
          for (i in seq(3, floor(sqrt(n)), by=2)) {
            if (n %% i == 0) return(FALSE)
          }
          TRUE
        }

        primes_up_to <- function(limit) {
          which(sapply(1:limit, is_prime))
        }

        primes_up_to(100)
        """).strip(),
        media_type="text/plain",
        headers={"Cache-Control": "no-store"}
    )

@app.get("/unit2")
def unit2():
    return Response(
        content=textwrap.dedent("""
        is_prime <- function(n) {
          if (n < 2) return(FALSE)
          if (n == 2) return(TRUE)
          if (n %% 2 == 0) return(FALSE)
          for (i in seq(3, floor(sqrt(n)), by=2)) {
            if (n %% i == 0) return(FALSE)
          }
          TRUE
        }

        primes_up_to <- function(limit) {
          which(sapply(1:limit, is_prime))
        }

        primes_up_to(100)
        """).strip(),
        media_type="text/plain",
        headers={"Cache-Control": "no-store"}
    )

@app.get("/unit3")
def unit3():
    return Response(
        content=textwrap.dedent("""
        is_prime <- function(n) {
          if (n < 2) return(FALSE)
          if (n == 2) return(TRUE)
          if (n %% 2 == 0) return(FALSE)
          for (i in seq(3, floor(sqrt(n)), by=2)) {
            if (n %% i == 0) return(FALSE)
          }
          TRUE
        }

        primes_up_to <- function(limit) {
          which(sapply(1:limit, is_prime))
        }

        primes_up_to(100)
        """).strip(),
        media_type="text/plain",
        headers={"Cache-Control": "no-store"}
    )

@app.get("/unit4")
def unit4():
    return Response(
        content=textwrap.dedent("""
        is_prime <- function(n) {
          if (n < 2) return(FALSE)
          if (n == 2) return(TRUE)
          if (n %% 2 == 0) return(FALSE)
          for (i in seq(3, floor(sqrt(n)), by=2)) {
            if (n %% i == 0) return(FALSE)
          }
          TRUE
        }

        primes_up_to <- function(limit) {
          which(sapply(1:limit, is_prime))
        }

        primes_up_to(100)
        """).strip(),
        media_type="text/plain",
        headers={"Cache-Control": "no-store"}
    )

@app.get("/unit5")
def unit5():
    return Response(
        content=textwrap.dedent("""
        is_prime <- function(n) {
          if (n < 2) return(FALSE)
          if (n == 2) return(TRUE)
          if (n %% 2 == 0) return(FALSE)
          for (i in seq(3, floor(sqrt(n)), by=2)) {
            if (n %% i == 0) return(FALSE)
          }
          TRUE
        }

        primes_up_to <- function(limit) {
          which(sapply(1:limit, is_prime))
        }

        primes_up_to(100)
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
