function Ano(){
    var n = (new Date()).getFullYear()
    var select = document.getElementById("ano");
    for(var i = n; i>=1900; i--)select.options.add(new Option(i,i));

};
window.onload = Ano;