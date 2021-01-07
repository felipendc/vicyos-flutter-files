import 'package:flutter/material.dart';
import 'dart:math';

void main() {
  runApp(
    DicePage(),
  );
}

class DicePage extends StatefulWidget {
  @override
  _DicePageState createState() => _DicePageState();
}

class _DicePageState extends State<DicePage> {
  int leftButtonPressed = 1;
  int rightButtonPressed = 1;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: Colors.teal,
        appBar: AppBar(
          centerTitle: true,
          title: Text('My Dice App From Scratch!'),
          backgroundColor: Colors.teal,
        ),
        body: Center(
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Expanded(
                child: Padding(
                  padding: EdgeInsets.all(16),
                  child: FlatButton(
                    padding: EdgeInsets.all(0),
                    child: Image(
                      image: AssetImage('images/dice$leftButtonPressed.png'),
                    ),
                    onPressed: () {
                      setState(
                        () {
                          // By adding both variables, it will refresh both buttons!
                          rightButtonPressed = Random().nextInt(6) + 1;
                          leftButtonPressed = Random().nextInt(6) + 1;
                        },
                      );
                    },
                  ),
                ),
              ),
              Expanded(
                child: Padding(
                  padding: EdgeInsets.all(16),
                  child: FlatButton(
                    padding: EdgeInsets.all(0),
                    child: Image(
                      image: AssetImage('images/dice$rightButtonPressed.png'),
                    ),
                    onPressed: () {
                      setState(() {
                        // By adding both variables, it will refresh both buttons!
                        leftButtonPressed = Random().nextInt(6) + 1;
                        rightButtonPressed = Random().nextInt(6) + 1;
                      });
                    },
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
