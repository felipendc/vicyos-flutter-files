import 'package:flutter/material.dart';
import '../constants.dart';

class BottomButton extends StatelessWidget {
  const BottomButton({
    @required this.onTap,
    @required this.buttonTitle,
    this.colourGender,
  });

  final Function onTap;
  final String buttonTitle;
  final Color colourGender;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        child: Align(
          alignment: Alignment(0, -0.50),
          child: Text(
            buttonTitle,
            style: kLargeButtonTextStyle,
          ),
        ),
        margin: EdgeInsets.only(top: 10),
        height: kbottomContainerHeight,
        // color: kactiveCardColour, colourGender
        color: colourGender,

        width: double.infinity,
      ),
    );
  }
}
