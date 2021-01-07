import 'package:bmi_calculator/xylophone.dart';
import 'package:flutter/material.dart';
import 'bmi_screen.dart';
import 'xylophone.dart';

class Screen0 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        leading: Text(""),
        centerTitle: true,
        backgroundColor: Colors.purple,
        title: Text('Tela Principal'),
      ),
      body: Center(
        child: Column(
          children: <Widget>[
            RaisedButton(
              color: Colors.red,
              child: Text('Open BMICalculator'),
              onPressed: () {
                //Navigate to Screen 1
                Navigator.push(context,
                    MaterialPageRoute(builder: (context) => BMICalculator()));
              },
            ),
            RaisedButton(
              color: Colors.blue,
              child: Text('Open XylophoneApp'),
              onPressed: () {
                //Navigate to Screen 2
                Navigator.push(context,
                    MaterialPageRoute(builder: (context) => XylophoneApp()));
              },
            ),
          ],
        ),
      ),
    );
  }
}
