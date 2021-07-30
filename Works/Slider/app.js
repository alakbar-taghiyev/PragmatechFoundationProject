let img=document.querySelector('.slide img');
let images=[
    'img/nature01.jpg',
    'img/nature02.jpg',
    'img/nature03.jpg'
]

let count=0;
function goPrev(){
    if(count<2){
        img.setAttribute('src',images[2])
        count++
    }else{
        img.setAttribute('src',images[count-1])
        count--
    }
}

function goNext(){
    if(count>2){
        img.setAttribute('src',images[0])
        count=0
    }else{
        img.setAttribute('src',images[count])
        count++
    }
}