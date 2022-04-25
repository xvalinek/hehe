const liczby = document.querySelectorAll('.liczba')
const operatory = document.querySelectorAll(".operator")
const wyczysc = document.querySelector(".wyczysz")
const usun = document.querySelector(".usun")
const rownosc = document.querySelector(".rownosc")
const wynikPoprzednie = document.querySelector(".poprzednie-dzialanie")
const wynikAktualne = document.querySelector(".aktualne-dzialanie")

var aktualneDzialanie = " "
var poprzednieDzialanie = " "
var operacja = undefined

const zaktualizujWynik = () => {
    wynikAktualne.innerText = aktualneDzialanie
    wynikPoprzednie.innerText = poprzednieDzialanie
}

const dodajLiczbe = (liczba) => {
    aktualneDzialanie = aktualneDzialanie.toString() + liczba.toString()
}

liczby.forEach((liczba) => {
    liczba.addEventListener("click", () => {
        dodajLiczbe(liczba.innerText)
        zaktualizujWynik()
    })
})