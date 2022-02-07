console.log("dev-test-free" );
console.log(window.parent.location);
if (window.top.location.host != "localhost") {
    var antiClickjack = document.getElementById("antiClickjack");
    antiClickjack.parentNode.removeChild(antiClickjack);
} else {
    top.location = self.location;
}
