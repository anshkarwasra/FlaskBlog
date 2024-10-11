




//event listner for blog-icons
let  cards = Array.from(document.querySelectorAll(".PageCard"));
let pages = Array.from(document.querySelector(".blogs").children);
console.log(pages);

cards.forEach((e)=>{
    e.addEventListener("click",()=>{
        for(let i=0;i < pages.length;i++){
            (pages[i]).style.display = "none";
            (cards[i]).classList.remove("bGpeach");
            (cards[i]).classList.add("bGgrey");

        }
        (pages[Number(e.attributes.target.value)]).style.display = "flex";
        e.classList.remove("bGgrey")
        e.classList.add("bGpeach");
        console.log("flex");
    })
})


//event listner for blogPages

let blogPages = document.querySelectorAll(".leftBlogEntry");
let blogPagesImages = document.querySelectorAll(".blogImgList");
let blogDes = Array.from(document.querySelectorAll(".blogDesicription"));
blogPages.forEach((e)=>{
    e.addEventListener("click",()=>{
        blogPagesImages.forEach((l)=>{
            (l.firstElementChild).classList.add("filter-green");
            (l.firstElementChild).classList.remove("filter-white");
        })
        for(let i=0;i<blogPages.length;i++){
            (blogPages[i]).classList.remove("bGblue","clrWhite");
            (blogDes[i]).style.display = "none";
        }
        e.classList.add("bGblue","clrWhite");
        (Array.from(((Array.from(e.children))[1]).children)).forEach((eli)=>{
            (eli.firstElementChild).classList.add("filter-white");
            (eli.firstElementChild).classList.remove("filter-green");
        })
        blogDes[Number(e.attributes.target.value)].style.display = "block";
    })
})