console.log("conectou");

acertos = 10;
erros = 20;

var ctx = document.getElementById("myChart").getContext("2d");
var myChart = new Chart(ctx, {
  type: "doughnut",
  data: {
    labels: ["Acertos", "Erros"],
    datasets: [
      {
        label: "# of Votes",
        data: [numAcertos, numErros], //substitua numAcertos e numErros pelos valores desejados
        backgroundColor: ["rgba(255, 99, 132, 0.2)", "rgba(54, 162, 235, 0.2)"],
        borderColor: ["rgba(255, 99, 132, 1)", "rgba(54, 162, 235, 1)"],
        borderWidth: 1,
      },
    ],
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
  },
});
