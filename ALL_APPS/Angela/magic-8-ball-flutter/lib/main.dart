import 'package:flutter/material.dart';
import 'dart:math';
import 'package:flutter/rendering.dart';

void main() {
  runApp(
    MagicBoll(),
  );
}

class MagicBoll extends StatefulWidget {
  @override
  _MagicBollState createState() => _MagicBollState();
}

class _MagicBollState extends State<MagicBoll> {
  int changeQuestion = 1;
  void pickQuestion() {
    setState(() {
      changeQuestion = Random().nextInt(5) + 1;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: Colors.blueAccent[400],
        appBar: AppBar(
          backgroundColor: Colors.blueAccent[400],
          centerTitle: true,
          title: Text('Ask Me Anything'),
        ),
        body: Center(
          child: Container(
            child: Row(
              children: [
                Expanded(
                  child: Padding(
                    padding: const EdgeInsets.all(0),
                    child: FlatButton(
                      onPressed: () {
                        pickQuestion();
                      },
                      padding: EdgeInsets.all(16),
                      child: Image(
                        image: AssetImage('images/ball$changeQuestion.png'),
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
