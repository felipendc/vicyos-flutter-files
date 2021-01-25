// import 'dart:io';

/*

A ideia desse programa consiste de:

Pegar o resultado da API do openweathermap usando a latidude e longitude do usuário, 
formatar o resultado da API para o formato json usando o jsonDecode e verificar deu erro
caso sim, retornará o erro usando o "statusCode" do "http.dart" e cado o resultado seja 200
que significa que deu certo, e então retornará o body da API.

O resultado do body da API já convertida para json será usada para usar para verificar o resultado
do tempo.



*/

void main() {
  performTasks();
}

void performTasks() async {
  task1();
  String task2Result = await task2();
  task3(task2Result);
}

void task1() {
  String result = 'task 1 data';
  print(result);
}

Future task2() async {
  Duration threeSeconds = Duration(seconds: 5);
  // sleep(threeSeconds);
  String result;

  await Future.delayed(threeSeconds, () {
    result = 'task 2 data';
    print(result);
  });
  return result;
}

void task3(String task2Data) {
//  String result = 'task 3 data';
  print('Task 3 complete with $task2Data');
}

/*

  Nada a ver por enquanto" looding_screen
      // var longitude = jsonDecode(data)["coord"]["lon"]; // ["lat"]
      // print(longitude);

      // var latitude = jsonDecode(data)["coord"]["lat"];
      // print(latitude);

      // var weatherDescription = jsonDecode(data)["weather"][0]["description"];

*/
