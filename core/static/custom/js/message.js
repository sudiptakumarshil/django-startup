function alertErrorMessage(message = null) {
    Swal.fire({
        icon: "error",
        title: "Oops...",
        text: message,
    });
}