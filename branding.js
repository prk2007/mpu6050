if (window.top.location.host != "https://dev-test-free.pantheonsite.io/") {
    var antiClickjack = document.getElementById("antiClickjack");
    antiClickjack.parentNode.removeChild(antiClickjack);
} else {
    top.location = self.location;
}
