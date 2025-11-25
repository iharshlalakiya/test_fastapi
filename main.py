from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import textwrap

app = FastAPI()

@app.get("/unit1")
def unit1():
    return textwrap.dedent("""
    factorial_func <- function(n) {
      if (n == 0) return(1)
      prod(1:n)
    }

    factorial_func(10)
    """).strip()

@app.get("/unit2")
def unit2():
    return textwrap.dedent("""
    factorial_func <- function(n) {
      if (n == 0) return(1)
      prod(1:n)
    }

    factorial_func(10)
    """).strip()

@app.get("/unit3")
def unit3():
    return textwrap.dedent("""
    factorial_func <- function(n) {
      if (n == 0) return(1)
      prod(1:n)
    }

    factorial_func(10)
    """).strip()

@app.get("/unit4")
def unit4():
    return textwrap.dedent("""
    factorial_func <- function(n) {
      if (n == 0) return(1)
      prod(1:n)
    }

    factorial_func(10)
    """).strip()

@app.get("/unit5")
def unit5():
    return textwrap.dedent("""
    factorial_func <- function(n) {
      if (n == 0) return(1)
      prod(1:n)
    }

    factorial_func(10)
    """).strip()

@app.get("/")
def home():
    return textwrap.dedent("""
    tari masi no piko
    """).strip()
