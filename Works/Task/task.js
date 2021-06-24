let arr = [1,45,67,23,78,34,45,67,12,457]

//masssivdeki tek eded sayini tapin 

let tek_eded_sayi = 0;
for(i=0; i<arr.length; i++) {
    if(arr[i]%2 !==0) {
        tek_eded_sayi++
    }
}
console.log(tek_eded_sayi)

//masssivdeki cut eded sayini tapin

let cut_eded_sayi = 0;
for(i=0; i<arr.length; i++) {
    if(arr[i]%2 ==0) {
        cut_eded_sayi++
    }
}
console.log(cut_eded_sayi)

//masssivdeki ededlerin cemini tapin

let edelerin_cemi = 0;
for(i=0; i<arr.length; i++) {
    edelerin_cemi = edelerin_cemi + arr[i]
}
console.log(edelerin_cemi)

//massivdeki sondan 4 elementin cemini tapin - 1ci metod

let sondan_4_elementin_cemi = 0;
for(i=6; i<=9; i++) {
    sondan_4_elementin_cemi = sondan_4_elementin_cemi + arr[i]
}
console.log(sondan_4_elementin_cemi)

//massivdeki sondan 4 elementin cemini tapin - 2ci metod

let sondan_4_elementin_toplami = 0;
for(i=arr.length - 1; i>=arr.length - 4; i--) {
    sondan_4_elementin_toplami = sondan_4_elementin_toplami + arr[i]
}
console.log(sondan_4_elementin_toplami)

//massivdeki en boyuk ededi tapin

let en_boyuk_eded = 0;
for(i=0; i<arr.length; i++) {
    
}
//massivde tekrarlanan ededleri ekrana cap edin




