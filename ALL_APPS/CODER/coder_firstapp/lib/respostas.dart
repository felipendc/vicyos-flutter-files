import 'package:flutter/material.dart';

class Respostas extends StatelessWidget {
  final String texto;
  final Function() quandoSelecionado;

  const Respostas({this.texto, this.quandoSelecionado});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      child: RaisedButton(
        color: Colors.blue,
        textColor: Colors.white,
        child: Text(texto),
        // "Resposta 2"
        onPressed: quandoSelecionado,
      ),
    );
  }
}
