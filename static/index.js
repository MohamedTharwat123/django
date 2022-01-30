
var NBE = document.querySelector("#pay-form-location")

NBE.SetupPayment({
    AppendToElementId: "pay-form-location",
    // AuthKey: "#AuthKey",
    DefaultErrorUrl: "https://www.yourdomain.com/handleerror"
});


// AuthKey: $("#AuthKey").val(),