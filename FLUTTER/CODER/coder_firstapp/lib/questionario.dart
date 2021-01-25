import 'package:flutter/material.dart';
import './questao.dart';
import './respostas.dart';

class Questionario extends StatelessWidget {
  final List<Map<String, Object>> perguntas;
  final int perguntaSelecionada;
  final void Function(int) botaoClicado;

  Questionario({
    @required this.perguntas,
    @required this.perguntaSelecionada,
    @required this.botaoClicado,
  });

  @override
  Widget build(BuildContext context) {
    List<Map<String, Object>> respostas =
        perguntas[perguntaSelecionada]['respostas'];
    List<Widget> widget = respostas.map((resp) {
      return Respostas(
          texto: resp['texto'],
          quandoSelecionado: () => botaoClicado(resp['pontuacao']));
    }).toList();
    return Column(
      children: [Questao(perguntas[perguntaSelecionada]['texto']), ...widget],
    );
  }
}
