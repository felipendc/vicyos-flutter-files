import 'package:flutter/material.dart';
import 'package:bmi_calculator/constants.dart';
import '../components/reusable_card.dart';
import 'package:bmi_calculator/components/bottom_button.dart';
import '../components/getSliderColours.dart';
import 'package:bmi_calculator/screens/input_page.dart';
import 'package:bmi_calculator/components/getSliderColours.dart';

class ResultsPage extends StatelessWidget {
  final String bmiResult;
  final String resultText;
  final String interpretation;

  ResultsPage({
    @required this.bmiResult,
    @required this.resultText,
    @required this.interpretation,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // appBar: AppBar(
      //   centerTitle: true,
      //   title: Text("BMI CALCULATOR"),
      // ),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          Expanded(
            child: Container(
              alignment: Alignment.bottomLeft,
              padding: EdgeInsets.all(15),
              child: Text(
                "Your result",
                style: TextStyle(
                  fontSize: 40,
                  fontWeight: FontWeight.bold,
                  color: getTopResultColor(selectedGender),
                ),
              ),
            ),
          ),
          Expanded(
            flex: 5,
            child: ReusableCard(
              colour: kactiveCardColour,
              cardChild: Column(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Center(
                    child: Text(
                      // "Normal",
                      resultText.toUpperCase(),
                      style: kResultTextStyle,
                    ),
                  ),
                  Text(
                    // "18.3",
                    bmiResult,
                    style: kBMITextStyle,
                  ),
                  Text(
                    // "Your BMI result is quite low, you should eat more!",
                    interpretation,
                    style: kBodyTextStyle,
                    textAlign: TextAlign.center,
                  ),
                ],
              ),
            ),
          ),
          BottomButton(
            colourGender: getBottomContainerColor(selectedGender),
            onTap: () {
              Navigator.pop(context);
            },
            buttonTitle: "RE-CALCULAR",
          )
        ],
      ),
    );
  }
}
