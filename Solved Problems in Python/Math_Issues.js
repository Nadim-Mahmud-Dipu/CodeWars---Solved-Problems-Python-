Math.round = function(number) {
    // TODO: fix this
   var x = number%1
   if(x<0.5) return number-x;
   else return (number-x)+1;
 };
 
 Math.ceil = function(number) {
    // TODO: fix this
   const x = number%1;
   //console.log(x);
   if(x>0) return (number-x)+1;
   else return number-x;
 };
 
 Math.floor = function(number) {
   var x = number%1
   
   if(x>0) return number-x;
   if(number ===0) return 0;
   if(x===0 && number>0) return number;
 };