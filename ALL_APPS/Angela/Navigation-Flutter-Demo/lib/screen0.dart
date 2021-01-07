import 'package:flutter/material.dart';
import 'screen1.dart';
import 'screen2.dart';

class Screen0 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.purple,
        title: Text('Tela Principal'),
      ),
      body: Center(
        child: Column(
          children: <Widget>[
            RaisedButton(
              color: Colors.red,
              child: Text('Ir para a tela 1'),
              onPressed: () {
                //Navigate to Screen 1
                Navigator.pushNamed(context, "/first");
              },
            ),
            RaisedButton(
              color: Colors.blue,
              child: Text('Ir para a tela 2'),
              onPressed: () {
                //Navigate to Screen 2
                Navigator.pushNamed(context, "/second");
              },
            ),
          ],
        ),
      ),
    );
  }
}

class Screen001 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: Text("Tela do App 001"),
      ),
      body: Center(
        child: RaisedButton(
          child: Text("Voltar para a Tela Principal"),
          onPressed: () {
            Navigator.pop(context);
          },
        ),
      ),
    );
  }
}

class Screen002 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: Text("Tela do App 002"),
      ),
      body: Center(
        child: RaisedButton(
          child: Text("Voltar para a Tela Principal"),
          onPressed: () {
            Navigator.pop(context);
          },
        ),
      ),
    );
  }
}
