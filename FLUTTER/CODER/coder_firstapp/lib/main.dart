// Pasta: 3
//  video 10 pra assistir

// Disciplina
// Trabalho duro
// Talento

import 'package:flutter/material.dart';
import './resultado.dart';
import './questionario.dart';

main(List<String> args) {
  runApp(_PerguntaApp());
}

class _PerguntaApp extends StatefulWidget {
  @override
  _PerguntaAppState createState() => _PerguntaAppState();
}

class _PerguntaAppState extends State<_PerguntaApp> {
  bool fimDasPerguntas = true;
  int _perguntaSelecionada = 0;
  var _pontuacaoTotal = 0;

  final _perguntas = const [
    {
      'texto': 'Qual é a sua cor favorita?',
      'respostas': [
        {'texto': 'Preto', 'pontuacao': 10},
        {'texto': 'Vermelho', 'pontuacao': 5},
        {'texto': 'Verde', 'pontuacao': 3},
        {'texto': 'Branco', 'pontuacao': 2},
      ],
    },
    {
      'texto': 'Qual é o seu animal favorito?',
      'respostas': [
        {'texto': 'Coelho', 'pontuacao': 10},
        {'texto': 'Cobra', 'pontuacao': 5},
        {'texto': 'Elefanete', 'pontuacao': 3},
        {'texto': 'Leão', 'pontuacao': 1},
      ],
    },
    {
      'texto': 'Qual é o seu instrutor favorito?',
      'respostas': [
        {'texto': 'Maria', 'pontuacao': 10},
        {'texto': 'Jão', 'pontuacao': 5},
        {'texto': 'Léo', 'pontuacao': 3},
        {'texto': 'Pedro', 'pontuacao': 1},
      ],
    }
  ];

// Verifica se numero de perguntas chegou ao fim e retorna
// um valor verdadeiro.
  bool estaFinalizado() {
    if (_perguntaSelecionada >= _perguntas.length - 1) {
      print('Não tem mais pergunta!');
      return true;
    } else {
      print('Ainda tem mais pergunta!');
      return false;
    }
  }

// Ir para a próxima pergunta e parar na última.
  void _proximaPergunta(int pontuacao) {
    if (_perguntaSelecionada < _perguntas.length - 1) {
      _perguntaSelecionada++;
      _pontuacaoTotal += pontuacao;
      print(_pontuacaoTotal);
    }
  }

// Verificar se as perguntas terminaram.
// Caso ainda exista mais perguntas, contua indo para a proxima pergunta.
// Se as perguntas acabaram exiba a tela de parabéns.
  void _botaoClicado(pontuacao) {
    // O setState((){}) Serve para atualizar /
    // redesenhar ou re-renderizar o widget na tela.
    setState(() {
      if (estaFinalizado() == true) {
        fimDasPerguntas = false;
      } else {
        _proximaPergunta(pontuacao);
        print(_perguntaSelecionada);
      }
    });
  }

  void _reiniciarQuestionario() {
    setState(() {
      fimDasPerguntas = true;
      _perguntaSelecionada = 0;
      _pontuacaoTotal = 0;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          centerTitle: true,
          title: Text('Perguntas'),
        ),
        body: fimDasPerguntas
            ? Questionario(
                perguntas: _perguntas,
                perguntaSelecionada: _perguntaSelecionada,
                botaoClicado: _botaoClicado)
            : Resultado(_pontuacaoTotal, _reiniciarQuestionario),
      ),
    );
  }
}
