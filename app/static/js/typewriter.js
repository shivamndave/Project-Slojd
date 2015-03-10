
// $(document).ready(function () {
//     function changeText(cont1, cont2, speed) {
//         var contents = $(cont1).contents().map(function () {
//             if (this.nodeType == 3) {
//                 if ($.trim(this.nodeValue).length) {
//                     return this.nodeValue.split("")
//                 }
//             } else {
//                 return $(this).clone().get();
//             }
//         }).get();
//         var i = 0;

//         function show() {
//             if (i < contents.length) {
//                 cont2.append(contents[i]);
//                 i = i + 1;
//             } else {
//                 clearInterval(Otimer)
//             }
//         };
//         var Otimer = setInterval(show, speed);
//     };
//     $(document).ready(function () {
//         changeText($("#TypeEffect p"), $(".p2"), 150);
//     });
// });