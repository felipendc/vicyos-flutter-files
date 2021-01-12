import 'product.dart';
import 'package:flutter/material.dart';
import '../data/dummy_data.dart';

class Products with ChangeNotifier {
  List<Product> _items = DUMMY_PRODUCTS;

  List<Product> get items => [..._items];

  int get itemsCount {
    return _items.length;
  }

  List<Product> get favoriteItems {
    return _items.where((prod) => prod.isFavorite).toList();
  }

  void addProduct(Product product) {
    _items.add(product);
    notifyListeners();
  }
}

// // Usar apenas como referência!!!
//
//  if (_showFavoriteOnly) {
//       // // Essa função vai verificar se vc marcou o "_showFavoriteOnly" como true
//       // // caso seja verdadeiro ele vai retornar apenas os Favoritos caso o contrário, ele
//       // // vai retornar apenas a lista.
//       // //

//       // Esse método "where" serve para filtrar (filtra e retorna) os items
//       // que foram marcados como verdadeiro (true).
//       //
//       // DICA o " Where é do tipo booleano"
//       //
//       // O prod é apenas um nome que eu usei para se referir ao product ou produto.
//       //
//       // No caso dessa parte do código o "Where" vai verificar dentro de Product() pelos
//       // instâncias dos items que tem a vareável "isFavorite" marcada como true e
//       // retornará-los como uma lista.
//       return _items.where((prod) => prod.isFavorite).toList();
//     }

//     // Esses 3 pontinhos logo abaixo significa (extraction) ele serve para extrair os
//     // items de uma lista em um novo local sem afetar a lista original.
//     // É como se ele fizesse uma cópia da lista original.
//     return [..._items];
//   }

// bool _showFavoriteOnly = false;

// void showFavoriteOnly() {
//   _showFavoriteOnly = true;

//   // notifyListeners() Ele vai detectar as mudanças feitas dentro de _showFavoriteOnly.
//   notifyListeners();
// }

// void showAll() {
//   _showFavoriteOnly = false;

//   // notifyListeners() Ele vai detectar as mudanças feitas dentro de _showFavoriteOnly.
//   notifyListeners();
// }
