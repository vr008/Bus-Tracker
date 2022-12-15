document.addEventListener("DOMContentLoaded", () => {
    const ham = document.getElementById("hamButton");
    ham.addEventListener("click", () =>{
        const menu = document.getElementById("menu");
        console.log(menu.style.display);
        if (menu.style.display === "none"){
            menu.style.display = "flex";
        }
        else{
            menu.style.display = "none";
        } 
    });
});