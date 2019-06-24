function ChangeContent(){
var selectorAdExtra = document.getElementById("AdvertExtraOption");
var valueStated = selectorAdExtra.options[selectorAdExtra.selectedIndex].value;    
var divImp = document.getElementById("AdExtra");

if(valueStated == 1){
var label = document.createElement('label');
var input = document.createElement('input');
input.type = "input";
input.className = "form-control";
input.id = "AdExtraInp";
label.for = "AdExtraInp";
label.innerHTML = "Please write down the unit id";
divImp.appendChild(label);
divImp.appendChild(input);


}
if(valueStated != 1){
    divImp.innerHTML = "";
}
}



