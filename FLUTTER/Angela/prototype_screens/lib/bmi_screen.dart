import 'package:flutter/material.dart';
import 'constants.dart';
import 'input_page.dart';
import 'screen0.dart';

void main() {
  runApp(
    Screen0(),
  );
}

class BMICalculator extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData.dark().copyWith(
        // Change The Slider Colours at => Constants.dart
        sliderTheme: SliderTheme.of(context).copyWith(
          activeTrackColor: kactiveSliderBaseColour,
          inactiveTrackColor: kinactiveSliderBaseColour,
          thumbColor: ksliderBaseThumbColour,
          overlayColor: ksliderBaseColourForOverlay,
        ),
        primaryColor: Color(0xFF0A0E21),
        scaffoldBackgroundColor: Color(0xFF0A0E21),
      ),
      home: InputPage(),
    );
  }
}
