import streamlit as st

st.title("Klausur")

st.subheader("Aufgabe 1")

zahl1 = st.number_input("Zahl1", value=2)
zahl2 = st.number_input("Zahl2", value=1)

a1Btn = st.button("Aufgabe 1")

if a1Btn:
    st.write(
        *sorted([zahl1, zahl2])
    )

st.subheader("Aufgabe 2")

kreditSumme = st.number_input("Kreditsumme", value=500)
a2Btn = st.button("Aufgabe 2")

if a2Btn:
    st.text(
    f"Kreditsumme nach einem Jahr: {kreditSumme * 1.03}€"
    )

st.subheader("Aufgabe 3")

basis = st.number_input("Basis", value=2)
exponent = st.number_input("Exponent", value=4)

a3Btn = st.button("Aufgabe 3")

if a3Btn:
    # option a) for-Schleife
    myBasisForLoop = 1
    for i in range(exponent):
        myBasisForLoop = myBasisForLoop * basis

    # option b) while-Schleife
    myBasisWhileLoop = 1
    counter = exponent
    while counter:
        myBasisWhileLoop = myBasisWhileLoop * basis
        counter -= 1

    st.text(f"""
    Basis: {basis}
    Exponent: {exponent}
    Ergebnis for-Schleife: {myBasisForLoop}
    Ergebnis while-Schleife: {myBasisWhileLoop}
    Kontrolle: {basis ** exponent}
        """)


st.subheader("Aufgabe 4")

def fibonacci(l):
    k, j = 0, 1
    st.success(k)
    st.success(j)
    for i in range(l):
        n = k+j
        k, j = j, k
        j = n
        st.success(n)

fibonacciLaenge = st.slider("Fibonacci Länge", value=11)
a4Btn = st.button("Aufgabe 4")

if a4Btn:
    fibonacci(fibonacciLaenge)

st.subheader("Aufgabe 5")

name = st.text_input(label="Text", value="CSAIPRALKAINACZEYLVOST")

a5Btn = st.button("Aufgabe 5")

if a5Btn:
    st.text(name[1::2])

st.subheader("Aufgabe 6")

nameList = ['Emily', 'Hannah', 'Madison', 'Ashley', 'Sarah', 'Alexis', 'Samantha', 'Jessica', 'Elizabeth', 'Taylor', 'Lauren', 'Alyssa', 'Kayla', 'Abigail', 'Brianna', 'Olivia', 'Emma', 'Megan', 'Grace', 'Victoria']
st.text("Namen: " + " ".join(nameList))

a6Btn = st.button("Aufgabe 6")

if a6Btn:
    st.write(
        *[name for name in nameList if name[0] in ['A', 'M']]
    )

st.subheader("Aufabe 7")

a7Btn = st.button("Aufgabe 7")

if a7Btn:
    for i in range(1, 100+1):
        if i % 3 == 0 and i % 5 == 0:
            st.success("FizzBuzz")

        elif i % 3 == 0:
            st.success("Fizz")
        
        elif i % 5 == 0:
            st.success("Buzz")

        else:
            st.text(i)

st.subheader("Aufgabe 8")

def weihnachtsBaum(l = 6):
    w = 1 + 2 * (l - 1)

    for i in range(1, l + 1):
        st.text(
            ("*" * (1 + (i - 1) * 2)).center(w, "_") + "\n"
        )

    st.text("frohe Weihnachten")
    st.warning("Im Browser funktioniert der Weihnachtsbaum nur mit einem Füller statt den Leerzeichen. Siehe hierfür jupyter-Notebook")



a8Btn = st.button("Aufgabe 8")

if a8Btn:
    weihnachtsBaum(l=7)
