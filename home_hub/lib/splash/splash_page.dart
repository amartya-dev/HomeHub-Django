import 'package:flutter/material.dart';

class SplashPage extends StatelessWidget {
  @override
  Widget build (BuildContext context) {
    return Scaffold(
      body: Center(
        child: Text(
          'Home Hub',
          style: TextStyle(
            fontSize: 40.0
          ),
        ),
      ),
    );
  }
}
