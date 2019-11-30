const ROMAN_NUMERALS = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    4: "IV",
    5: "V",
    1: "I",
};

function toRoman(number) {
    if (number === 0)
        return "";

    for (let index of Object.keys(ROMAN_NUMERALS).reverse())
        if (number >= index)
            return ROMAN_NUMERALS[index] + toRoman(number - index);
}

document.addEventListener("DOMContentLoaded", () => {
    let chapters = document.querySelectorAll("nav.wy-nav-side p.caption");
    let menuItems = document.querySelectorAll("nav.wy-nav-side p.caption + ul");

    menuItems.forEach((ul) => {
        if (ul.className === "current")
            ul.style.display = "block";
        else
            ul.style.display = "none";
    });

    chapters.forEach((chapter, i) => {
        let roman = toRoman(i+1);
        chapter.innerHTML = `${roman}. ${chapter.innerHTML}`;

        chapter.onclick = () => {
            let ul = chapter.nextElementSibling;

            if (ul.style.display !== "block")
                ul.style.display = "block";
            else
                ul.style.display = "none";
        }
    });
});
